import csv
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

csv_files = sorted(glob.glob('tests/csv/*.csv') + glob.glob('Tests/*.csv'))
for f in csv_files:
    rows = list(csv.reader(open(f, encoding='utf-8-sig')))
    headers = [h.strip().strip('"').replace('\ufeff','') for h in rows[0]]
    notes_idx = headers.index('Notes') if 'Notes' in headers else -1
    title_idx = headers.index('Title') if 'Title' in headers else -1
    id_idx = headers.index('ID') if 'ID' in headers else -1
    
    print(f"\n=== {f} ===")
    reqs_found = set()
    unmatched = []
    
    for r in rows[1:]:
        tc_id = r[id_idx] if id_idx != -1 and id_idx < len(r) else ''
        title = r[title_idx] if title_idx != -1 and title_idx < len(r) else ''
        notes = r[notes_idx] if notes_idx != -1 and notes_idx < len(r) else ''
        
        # Search for Mxx-Fxx in notes or title
        m = re.findall(r'M\d+-F\d+', notes + " " + title)
        if m:
            reqs_found.update(m)
        else:
            unmatched.append((tc_id, title, notes))
            
    print(f"  Mapped Features: {sorted(list(reqs_found))}")
    print(f"  Unmatched Count: {len(unmatched)}")
    if unmatched:
        for u in unmatched:
            print(f"    - {u[0]}: {u[1]} | Notes: {u[2]}")
