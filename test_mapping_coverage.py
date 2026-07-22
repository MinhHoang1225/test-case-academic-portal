import os
import sys
import csv
import glob
import re

sys.stdout.reconfigure(encoding='utf-8')

feature_catalog = {}
for f in sorted(glob.glob('Docs/module*.md')):
    mod_num = re.search(r'module(\d+)\.md', f).group(1)
    mod_key = f"M{int(mod_num):02d}"
    content = open(f, encoding='utf-8').read()
    matches = re.findall(r'\|\s*(M\d+-F\d+)\s*\|\s*([^|]+)\s*\|', content)
    for fid, fname in matches:
        feature_catalog[fid] = fname.strip()

def get_exact_feature(tc_id, title, notes, mod_key):
    # Check explicit code first
    m = re.findall(r'M\d+-F\d+', notes + " " + title)
    if m:
        fid = m[0]
        if fid in feature_catalog:
            return fid, feature_catalog[fid]

    # Specific TC mappings by ID or content patterns
    full = (title + " " + notes).lower()

    if mod_key == "M01":
        if "access" in full or "domain" in full:
            return "M01-SEC", "Access Control & Security"
    elif mod_key == "M02":
        if "access" in full or "scan management" in full:
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
        if tc_id in ["TC-M04-014", "TC-M04-015", "TC-M04-018"]:
            return "M04-F01", feature_catalog["M04-F01"]
        elif tc_id in ["TC-M04-016", "TC-M04-017"]:
            return "M04-F02", feature_catalog["M04-F02"]
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

# Run mapping report
unmapped_total = 0
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
        
        fid, fname = get_exact_feature(tc_id, title, notes, mod_key)
        if "GEN" in fid:
            unmapped_total += 1
            print(f"Unmapped: {tc_id} | {title} | {notes}")
        key = f"{fid} - {fname}"
        feature_counts[key] = feature_counts.get(key, 0) + 1
        
    print(f"\n=== {os.path.basename(f)} ({len(rows)-1} TCs) ===")
    for k, v in sorted(feature_counts.items()):
        print(f"  {k}: {v} TCs")

print(f"\nTotal GEN/Unmapped: {unmapped_total}")
