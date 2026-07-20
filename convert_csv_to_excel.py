import os
import glob
import csv
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Colors
HEADER_BG = "1F4E78"        # Navy blue
HEADER_FG = "FFFFFF"        # White text
ZEBRA_BG  = "F8FAFC"        # Light slate/blue tint
BORDER_COLOR = "CBD5E1"     # Light gray border

PRIORITY_MAP = {
    "HIGH": "HIGH",
    "CAO": "HIGH",
    "MEDIUM": "MEDIUM",
    "TRUNG BÌNH": "MEDIUM",
    "TRUNG BINH": "MEDIUM",
    "LOW": "LOW",
    "THẤP": "LOW",
    "THAP": "LOW"
}

PRIORITY_STYLES = {
    "HIGH": {
        "fill": PatternFill(start_color="FCE8E6", end_color="FCE8E6", fill_type="solid"),
        "font": Font(name="Segoe UI", size=10, bold=True, color="A50E0E")
    },
    "MEDIUM": {
        "fill": PatternFill(start_color="FEF7E0", end_color="FEF7E0", fill_type="solid"),
        "font": Font(name="Segoe UI", size=10, bold=True, color="B06000")
    },
    "LOW": {
        "fill": PatternFill(start_color="E6F4EA", end_color="E6F4EA", fill_type="solid"),
        "font": Font(name="Segoe UI", size=10, bold=True, color="137333")
    }
}

COLUMN_WIDTHS = {
    1: 15,  # ID
    2: 14,  # Module
    3: 32,  # Title
    4: 38,  # Objective
    5: 32,  # Preconditions
    6: 30,  # TestData
    7: 50,  # Steps
    8: 50,  # ExpectedResult
    9: 14,  # Priority
    10: 32  # Notes
}

def clean_cell_text(val):
    if val is None:
        return ""
    s = str(val).strip()
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    return s

def normalize_priority(val):
    v = str(val).strip().upper()
    return PRIORITY_MAP.get(v, None)

def format_worksheet(ws, headers, rows):
    ws.views.sheetView[0].showGridLines = True

    # Font definitions
    header_font = Font(name="Segoe UI", size=11, bold=True, color=HEADER_FG)
    header_fill = PatternFill(start_color=HEADER_BG, end_color=HEADER_BG, fill_type="solid")
    header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

    body_font = Font(name="Segoe UI", size=10, color="000000")
    thin_side = Side(border_style="thin", color=BORDER_COLOR)
    cell_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

    # Write Headers
    ws.row_dimensions[1].height = 28
    for col_num, h_name in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_num, value=h_name)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align
        cell.border = cell_border

    # Set Column Widths
    for col_idx, width in COLUMN_WIDTHS.items():
        if col_idx <= len(headers):
            col_letter = get_column_letter(col_idx)
            ws.column_dimensions[col_letter].width = width

    # Write Rows
    for row_idx, row_data in enumerate(rows, start=2):
        is_even = (row_idx % 2 == 0)
        row_fill = PatternFill(start_color=ZEBRA_BG, end_color=ZEBRA_BG, fill_type="solid") if not is_even else PatternFill(fill_type=None)
        
        max_lines = 1

        for col_idx, cell_value in enumerate(row_data, start=1):
            if col_idx > len(headers):
                break
            text = clean_cell_text(cell_value)
            cell = ws.cell(row=row_idx, column=col_idx, value=text)
            
            cell.font = body_font
            cell.border = cell_border

            # Horizontal alignment logic
            h_align = "left"
            if headers[col_idx-1] in ["ID", "Module", "Priority"]:
                h_align = "center"

            cell.alignment = Alignment(horizontal=h_align, vertical="top", wrap_text=True)

            # Priority column styling
            if headers[col_idx-1] == "Priority":
                p_norm = normalize_priority(text)
                if p_norm in PRIORITY_STYLES:
                    cell.fill = PRIORITY_STYLES[p_norm]["fill"]
                    cell.font = PRIORITY_STYLES[p_norm]["font"]
            else:
                if not is_even:
                    cell.fill = row_fill

            lines = text.count('\n') + 1
            if len(text) > 40:
                lines += len(text) // 40
            if lines > max_lines:
                max_lines = lines

        calc_height = max(22, min(180, max_lines * 15))
        ws.row_dimensions[row_idx].height = calc_height

    ws.auto_filter.ref = ws.dimensions

def read_csv_file(csv_path):
    rows = []
    headers = []
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if not row:
                continue
            if i == 0:
                headers = [h.strip().strip('"').replace('\ufeff', '') for h in row]
                headers = ["Preconditions" if h == "Precondition" else h for h in headers]
            else:
                rows.append(row)
    return headers, rows

def create_summary_sheet(wb, module_data):
    ws = wb.create_sheet(title="Summary", index=0)
    ws.views.sheetView[0].showGridLines = True

    # Title Banner
    ws.merge_cells("A1:E1")
    title_cell = ws.cell(row=1, column=1, value="Academic Portal - Comprehensive Test Case Suite Summary")
    title_cell.font = Font(name="Segoe UI", size=16, bold=True, color="FFFFFF")
    title_cell.fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 40

    total_test_cases = 0
    total_high = 0
    total_medium = 0
    total_low = 0
    module_summary_rows = []

    for mod_num, (mod_title, headers, rows) in enumerate(module_data, start=1):
        mod_tc_count = len(rows)
        p_col_idx = -1
        for idx, h in enumerate(headers):
            if h.lower() == "priority":
                p_col_idx = idx
                break
        
        high_cnt = 0
        med_cnt = 0
        low_cnt = 0
        if p_col_idx != -1:
            for r in rows:
                if p_col_idx < len(r):
                    p_norm = normalize_priority(r[p_col_idx])
                    if p_norm == "HIGH":
                        high_cnt += 1
                    elif p_norm == "MEDIUM":
                        med_cnt += 1
                    elif p_norm == "LOW":
                        low_cnt += 1

        total_test_cases += mod_tc_count
        total_high += high_cnt
        total_medium += med_cnt
        total_low += low_cnt

        module_summary_rows.append((mod_title, mod_tc_count, high_cnt, med_cnt, low_cnt))

    # Metric Cards Row
    metrics = [
        ("Total Modules", len(module_data), "1E293B", "F1F5F9"),
        ("Total Test Cases", total_test_cases, "1F4E78", "E2E8F0"),
        ("High Priority", total_high, "A50E0E", "FCE8E6"),
        ("Medium Priority", total_medium, "B06000", "FEF7E0"),
        ("Low Priority", total_low, "137333", "E6F4EA"),
    ]

    for idx, (label, val, fg_color, bg_color) in enumerate(metrics):
        l_cell = ws.cell(row=3, column=idx+1, value=label)
        l_cell.font = Font(name="Segoe UI", size=9, bold=True, color="555555")
        l_cell.alignment = Alignment(horizontal="center", vertical="center")
        
        v_cell = ws.cell(row=4, column=idx+1, value=val)
        v_cell.font = Font(name="Segoe UI", size=18, bold=True, color=fg_color)
        v_cell.fill = PatternFill(start_color=bg_color, end_color=bg_color, fill_type="solid")
        v_cell.alignment = Alignment(horizontal="center", vertical="center")
        thin_side = Side(border_style="thin", color="CBD5E1")
        v_cell.border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

    ws.row_dimensions[3].height = 20
    ws.row_dimensions[4].height = 35

    # Table Header for Module Breakdown (row 6)
    table_headers = ["Module Name", "Total Test Cases", "High Priority", "Medium Priority", "Low Priority"]
    ws.row_dimensions[6].height = 26
    for col_idx, th_name in enumerate(table_headers, start=1):
        cell = ws.cell(row=6, column=col_idx, value=th_name)
        cell.font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="2B3E50", end_color="2B3E50", fill_type="solid")
        cell.alignment = Alignment(horizontal="center" if col_idx > 1 else "left", vertical="center")
        thin_side = Side(border_style="thin", color="1E293B")
        cell.border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

    # Table Data Rows
    thin_border = Border(left=Side(style="thin", color="CBD5E1"),
                         right=Side(style="thin", color="CBD5E1"),
                         top=Side(style="thin", color="CBD5E1"),
                         bottom=Side(style="thin", color="CBD5E1"))

    for row_offset, (m_name, count, h_cnt, m_cnt, l_cnt) in enumerate(module_summary_rows, start=7):
        ws.row_dimensions[row_offset].height = 22
        vals = [m_name, count, h_cnt, m_cnt, l_cnt]
        is_even = (row_offset % 2 == 0)
        bg = "F8FAFC" if not is_even else "FFFFFF"
        fill = PatternFill(start_color=bg, end_color=bg, fill_type="solid")

        for col_idx, val in enumerate(vals, start=1):
            cell = ws.cell(row=row_offset, column=col_idx, value=val)
            cell.font = Font(name="Segoe UI", size=10)
            cell.alignment = Alignment(horizontal="left" if col_idx == 1 else "center", vertical="center")
            cell.fill = fill
            cell.border = thin_border

    # Total row at bottom
    tot_row_idx = 7 + len(module_summary_rows)
    ws.row_dimensions[tot_row_idx].height = 24
    tot_vals = ["Total", total_test_cases, total_high, total_medium, total_low]
    tot_fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
    tot_font = Font(name="Segoe UI", size=10, bold=True, color="000000")

    for col_idx, val in enumerate(tot_vals, start=1):
        cell = ws.cell(row=tot_row_idx, column=col_idx, value=val)
        cell.font = tot_font
        cell.alignment = Alignment(horizontal="left" if col_idx == 1 else "center", vertical="center")
        cell.fill = tot_fill
        cell.border = Border(top=Side(style="medium", color="1E293B"), bottom=Side(style="double", color="1E293B"), left=Side(style="thin", color="CBD5E1"), right=Side(style="thin", color="CBD5E1"))

    ws.column_dimensions["A"].width = 36
    ws.column_dimensions["B"].width = 20
    ws.column_dimensions["C"].width = 18
    ws.column_dimensions["D"].width = 18
    ws.column_dimensions["E"].width = 18

def process_csv_files(tests_dir):
    csv_files = sorted(glob.glob(os.path.join(tests_dir, "*.csv")))
    print(f"Found {len(csv_files)} CSV files in {tests_dir}:")

    master_wb = openpyxl.Workbook()
    master_wb.remove(master_wb.active)

    module_data = []

    for csv_path in csv_files:
        base_name = os.path.basename(csv_path)
        name_without_ext = os.path.splitext(base_name)[0]
        xlsx_path = os.path.join(tests_dir, f"{name_without_ext}.xlsx")

        headers, rows = read_csv_file(csv_path)
        print(f"  - Converting {base_name} ({len(rows)} test cases) -> {os.path.basename(xlsx_path)}")

        indiv_wb = openpyxl.Workbook()
        indiv_ws = indiv_wb.active
        sheet_title = name_without_ext.replace("_test_cases", "").capitalize()
        if len(sheet_title) > 30:
            sheet_title = sheet_title[:30]
        indiv_ws.title = sheet_title

        format_worksheet(indiv_ws, headers, rows)
        indiv_wb.save(xlsx_path)

        m_title = name_without_ext
        if "module" in m_title.lower():
            mod_part = m_title.lower().split("_")[0]
            mod_num = mod_part.replace("module", "")
            m_title = f"Module {mod_num}"
        else:
            m_title = name_without_ext[:30]

        master_ws = master_wb.create_sheet(title=m_title)
        format_worksheet(master_ws, headers, rows)

        module_data.append((m_title, headers, rows))

    create_summary_sheet(master_wb, module_data)

    master_xlsx_path = os.path.join(tests_dir, "academic_portal_all_test_cases.xlsx")
    master_wb.save(master_xlsx_path)
    print(f"\nCreated consolidated Master Workbook: {master_xlsx_path}")

if __name__ == "__main__":
    tests_directory = os.path.join(os.getcwd(), "Tests")
    process_csv_files(tests_directory)
