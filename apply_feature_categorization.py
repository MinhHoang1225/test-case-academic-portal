import os
import sys
import csv
import glob
import re

sys.stdout.reconfigure(encoding='utf-8')

# Feature Catalog from Docs
feature_catalog = {}
for f in sorted(glob.glob('Docs/module*.md')):
    mod_num = re.search(r'module(\d+)\.md', f).group(1)
    mod_key = f"M{int(mod_num):02d}"
    content = open(f, encoding='utf-8').read()
    matches = re.findall(r'\|\s*(M\d+-F\d+)\s*\|\s*([^|]+)\s*\|', content)
    for fid, fname in matches:
        feature_catalog[fid] = fname.strip()

def get_exact_feature(tc_id, title, notes, mod_key):
    # Search for explicit code in notes or title first
    m = re.findall(r'M\d+-F\d+', notes + " " + title)
    if m:
        fid = m[0]
        if fid in feature_catalog:
            return fid, feature_catalog[fid]

    full = (title + " " + notes).lower()

    if mod_key == "M01":
        if "access" in full or "domain" in full or "permission" in full:
            return "M01-SEC", "Access Control & Security"
    elif mod_key == "M02":
        if "access" in full or "scan management" in full or "permission" in full:
            return "M02-SEC", "Access Control & Security"
    elif mod_key == "M03":
        if tc_id == "TC-M03-013":
            return "M03-F04", feature_catalog["M03-F04"]
        elif tc_id in ["TC-M03-019", "TC-M03-020"]:
            return "M03-F06", feature_catalog["M03-F06"]
        elif tc_id == "TC-M03-021":
            return "M03-SEC", "Access Control & Security"
        elif tc_id == "TC-M03-022":
            return "M03-F03", feature_catalog["M03-F03"]
    elif mod_key == "M04":
        if tc_id in ["TC-M04-014", "TC-M04-015", "TC-M04-018", "TC-M04-019"]:
            return "M04-F01", feature_catalog["M04-F01"]
        elif tc_id in ["TC-M04-016", "TC-M04-017"]:
            return "M04-F02", feature_catalog["M04-F02"]
        elif tc_id in ["TC-M04-020", "TC-M04-021"]:
            return "M04-SEC", "Access Control & Security"
    elif mod_key == "M05":
        if tc_id in ["TC-M05-002", "TC-M05-003", "TC-M05-004", "TC-M05-005", "TC-M05-006", "TC-M05-007"]:
            return "M05-F01", feature_catalog["M05-F01"]
        elif tc_id in ["TC-M05-011", "TC-M05-012", "TC-M05-013"]:
            return "M05-F03", feature_catalog["M05-F03"]
        elif tc_id in ["TC-M05-018", "TC-M05-019"]:
            return "M05-F04", feature_catalog["M05-F04"]
        elif tc_id == "TC-M05-023":
            return "M05-F07", feature_catalog["M05-F07"]
    elif mod_key == "M06":
        if tc_id in ["TC-M06-009", "TC-M06-010"]:
            return "M06-F04", feature_catalog["M06-F04"]
        elif tc_id in ["TC-M06-012", "TC-M06-013"]:
            return "M06-F05", feature_catalog["M06-F05"]
        elif tc_id in ["TC-M06-015", "TC-M06-016", "TC-M06-017"]:
            return "M06-F06", feature_catalog["M06-F06"]
        elif tc_id in ["TC-M06-019", "TC-M06-020", "TC-M06-021", "TC-M06-022", "TC-M06-023", "TC-M06-024", "TC-M06-025", "TC-M06-026", "TC-M06-004"]:
            return "M06-F03", feature_catalog["M06-F03"]
        elif tc_id == "TC-M06-029":
            return "M06-F08", feature_catalog["M06-F08"]
        elif tc_id == "TC-M06-031":
            return "M06-F09", feature_catalog["M06-F09"]
    elif mod_key == "M07":
        if tc_id in ["TC-M07-002"]:
            return "M07-F02", feature_catalog["M07-F02"]
        elif tc_id in ["TC-M07-006", "TC-M07-010"]:
            return "M07-F03", feature_catalog["M07-F03"]
        elif tc_id in ["TC-M07-012", "TC-M07-015", "TC-M07-016"]:
            return "M07-F04", feature_catalog["M07-F04"]
        elif tc_id in ["TC-M07-018", "TC-M07-021", "TC-M07-022"]:
            return "M07-F05", feature_catalog["M07-F05"]
        elif tc_id in ["TC-M07-035", "TC-M07-036"]:
            return "M07-F07", feature_catalog["M07-F07"]
        elif tc_id in ["TC-M07-037", "TC-M07-038", "TC-M07-039"]:
            return "M07-SEC", "Access Control & Security"
    elif mod_key == "M08":
        if tc_id in ["TC-M08-018", "TC-M08-019"]:
            return "M08-F05", feature_catalog["M08-F05"]
        else:
            return "M08-F01", feature_catalog["M08-F01"]
    elif mod_key == "M09":
        if tc_id == "TC-M09-021":
            return "M09-UI", "User Interface & Responsiveness"
        elif tc_id == "TC-M09-022":
            return "M09-F01", feature_catalog["M09-F01"]
        elif tc_id == "TC-M09-023":
            return "M09-F02", feature_catalog["M09-F02"]

    return f"{mod_key}-GEN", "General Validation"

def process_csv_files():
    csv_files = sorted(glob.glob('tests/csv/*.csv') + glob.glob('Tests/*.csv'))
    for f in csv_files:
        mod_num = re.search(r'module(\d+)_', os.path.basename(f)).group(1)
        mod_key = f"M{int(mod_num):02d}"
        
        rows = list(csv.reader(open(f, encoding='utf-8-sig')))
        if not rows:
            continue
            
        old_headers = [h.strip().strip('"').replace('\ufeff','') for h in rows[0]]
        
        # Determine header indices
        id_idx = old_headers.index('ID') if 'ID' in old_headers else 0
        mod_idx = old_headers.index('Module') if 'Module' in old_headers else 1
        title_idx = old_headers.index('Title') if 'Title' in old_headers else 2
        notes_idx = old_headers.index('Notes') if 'Notes' in old_headers else -1

        # Build new rows with Feature ID and Feature Name inserted right after Module
        new_headers = old_headers[:mod_idx+1] + ["Feature ID", "Feature Name"] + old_headers[mod_idx+1:]
        
        # Check if already has Feature ID
        if "Feature ID" in old_headers:
            print(f"Skipping CSV rewrite for {f} (already has Feature ID)")
            continue

        new_rows = [new_headers]

        for r in rows[1:]:
            tc_id = r[id_idx] if id_idx < len(r) else ''
            title = r[title_idx] if title_idx < len(r) else ''
            notes = r[notes_idx] if notes_idx != -1 and notes_idx < len(r) else ''

            fid, fname = get_exact_feature(tc_id, title, notes, mod_key)

            row_new = r[:mod_idx+1] + [fid, fname] + r[mod_idx+1:]
            new_rows.append(row_new)

        # Write back updated CSV file with UTF-8 encoding
        with open(f, 'w', encoding='utf-8-sig', newline='') as out_f:
            writer = csv.writer(out_f, quoting=csv.QUOTE_ALL)
            writer.writerows(new_rows)

        print(f"Updated CSV: {os.path.basename(f)} -> Added Feature ID & Feature Name ({len(new_rows)-1} rows)")

if __name__ == "__main__":
    process_csv_files()
