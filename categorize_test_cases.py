import os
import sys
import csv
import glob
import re

sys.stdout.reconfigure(encoding='utf-8')

# Load Feature Catalog from Docs
feature_catalog = {}
for f in sorted(glob.glob('Docs/module*.md')):
    mod_num = re.search(r'module(\d+)\.md', f).group(1)
    mod_key = f"M{int(mod_num):02d}"
    content = open(f, encoding='utf-8').read()
    matches = re.findall(r'\|\s*(M\d+-F\d+)\s*\|\s*([^|]+)\s*\|', content)
    for fid, fname in matches:
        feature_catalog[fid] = fname.strip()

print("Feature Catalog loaded:", len(feature_catalog), "features.")

def determine_feature(tc_id, title, notes, mod_key):
    # 1. Search for explicit feature code in notes or title
    m = re.findall(r'M\d+-F\d+', notes + " " + title)
    if m:
        fid = m[0]
        fname = feature_catalog.get(fid, "Unknown Feature")
        return fid, fname

    # 2. Contextual mapping based on title/notes keywords
    title_lower = title.lower()
    notes_lower = notes.lower()
    full_text = title_lower + " " + notes_lower

    if mod_key == "M01":
        if "access" in full_text or "domain" in full_text or "permission" in full_text:
            return "M01-SEC", "Access Control & Security"
    elif mod_key == "M02":
        if "access" in full_text or "scan management" in full_text or "user role" in full_text:
            return "M02-SEC", "Access Control & Security"
    elif mod_key == "M03":
        if "decimal" in full_text or "upload" in full_text:
            return "M03-F04", feature_catalog["M03-F04"]
        elif "color" in full_text or "gpa color" in full_text:
            return "M03-F06", feature_catalog["M03-F06"]
        elif "access" in full_text or "user role" in full_text:
            return "M03-SEC", "Access Control & Security"
        elif "tbkt" in full_text or "formula" in full_text:
            return "M03-F03", feature_catalog["M03-F03"]
    elif mod_key == "M04":
        if "trend chart" in full_text:
            return "M04-F01", feature_catalog["M04-F01"]
        elif "badge" in full_text:
            return "M04-F02", feature_catalog["M04-F02"]
        elif "missing student" in full_text or "validation" in full_text:
            return "M04-F01", feature_catalog["M04-F01"]
        elif "draft" in full_text:
            return "M04-F04", feature_catalog["M04-F04"]
        elif "batch" in full_text:
            return "M04-F06", feature_catalog["M04-F06"]
    elif mod_key == "M05":
        if "unassigned" in full_text or "warning" in full_text:
            return "M05-F06", feature_catalog["M05-F06"]
        elif "assignment" in full_text or "assign" in full_text:
            return "M05-F04", feature_catalog["M05-F04"]
        elif "feedback" in full_text:
            return "M05-F07", feature_catalog["M05-F07"]
        elif "access" in full_text or "permission" in full_text:
            return "M05-SEC", "Access Control & Security"
    elif mod_key == "M06":
        if "hours" in full_text or "giờ" in full_text:
            return "M06-F06", feature_catalog["M06-F06"]
        if "email" in full_text:
            return "M06-F08", feature_catalog["M06-F08"]
        if "staff" in full_text or "quyền" in full_text or "role" in full_text:
            return "M06-F09", feature_catalog["M06-F09"]
        if "monday" in full_text or "thứ hai" in full_text or "thời gian" in full_text or "ngày" in full_text:
            return "M06-F04", feature_catalog["M06-F04"]
        if "danh sách" in full_text or "công việc" in full_text or "task" in full_text:
            return "M06-F05", feature_catalog["M06-F05"]
        if "validation" in full_text or "ngăn chặn" in full_text or "tạo" in full_text or "nộp" in full_text:
            return "M06-F03", feature_catalog["M06-F03"]
    elif mod_key == "M07":
        if "category" in full_text:
            return "M07-F02", feature_catalog["M07-F02"]
        if "course" in full_text or "khóa học" in full_text:
            return "M07-F03", feature_catalog["M07-F03"]
        if "session" in full_text or "bài học" in full_text:
            return "M07-F04", feature_catalog["M07-F04"]
        if "exam" in full_text or "bài kiểm tra" in full_text:
            return "M07-F05", feature_catalog["M07-F05"]
        if "csv" in full_text:
            return "M07-F07", feature_catalog["M07-F07"]
        if "quyền" in full_text or "role" in full_text or "access" in full_text or "domain" in full_text:
            return "M07-SEC", "Access Control & Security"
    elif mod_key == "M08":
        if "drive" in full_text or "storage" in full_text or "file" in full_text or "tải lên" in full_text or "upload" in full_text or "ảnh" in full_text:
            return "M08-F01", feature_catalog["M08-F01"]
        if "quyền" in full_text or "role" in full_text or "access" in full_text or "api" in full_text or "domain" in full_text:
            return "M08-F05", feature_catalog["M08-F05"]
    elif mod_key == "M09":
        if "responsive" in full_text or "di động" in full_text:
            return "M09-UI", "User Interface & Responsiveness"
        if "sign-out" in full_text or "phiên" in full_text or "session" in full_text:
            return "M09-F01", feature_catalog["M09-F01"]
        if "semester" in full_text or "học kỳ" in full_text or "grade" in full_text:
            return "M09-F02", feature_catalog["M09-F02"]

    return f"{mod_key}-GEN", "General / System Validation"

csv_files = sorted(glob.glob('tests/csv/*.csv') + glob.glob('Tests/*.csv'))
for f in csv_files:
    mod_num = re.search(r'module(\d+)_', os.path.basename(f)).group(1)
    mod_key = f"M{int(mod_num):02d}"
    rows = list(csv.reader(open(f, encoding='utf-8-sig')))
    headers = [h.strip().strip('"').replace('\ufeff','') for h in rows[0]]
    notes_idx = headers.index('Notes') if 'Notes' in headers else -1
    title_idx = headers.index('Title') if 'Title' in headers else -1
    id_idx = headers.index('ID') if 'ID' in headers else -1

    feature_counts = {}
    for r in rows[1:]:
        tc_id = r[id_idx] if id_idx != -1 and id_idx < len(r) else ''
        title = r[title_idx] if title_idx != -1 and title_idx < len(r) else ''
        notes = r[notes_idx] if notes_idx != -1 and notes_idx < len(r) else ''
        
        fid, fname = determine_feature(tc_id, title, notes, mod_key)
        key = f"{fid} - {fname}"
        feature_counts[key] = feature_counts.get(key, 0) + 1
        
    print(f"\n=== {os.path.basename(f)} ({len(rows)-1} TCs) ===")
    for k, v in sorted(feature_counts.items()):
        print(f"  {k}: {v} TCs")
