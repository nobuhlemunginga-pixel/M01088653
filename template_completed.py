"""
RECORD CHECK  -  my version
===========================

Name  : Philippa Munginga
Lane  :  AI 
Date  : 18/10/2026

Run it:   python template.py

"""

# =================================================================== FUNCTIONS
def check_record(value, limit):
    """Return difference, percent, andstatus."""
    diff = value - limit
    percent = (value / limit) * 100
    status = "OVER LIMIT" if value > limit else "OK"
    return diff, percent, status

def print_report(label, value, limit, diff, percent, status):
    """Print one report line neatly."""
    print(f"{label}: {status} (value={value}, limit={limit}, diff={diff}, percent={percent:.1f}%)")

def load_records(path):
    """Load records from a file into a lists of dicts."""
    records = []
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                label, value, limit = line.split(",")
                records.append({
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                })
    except FileNotFoundError:
        print(f"{path} not found.")
        return []
    return records


# ====================================================================== STORE

records = [
    {"label": "survey_2026", "value": 1187, "limit": 1200},
    {"label": "dataset_A", "value": 900, "limit": 850},
    {"label": "dataset_B", "value": 450, "limit":500},
]

records_from_file = load_records("records_sample.txt")

records_for_results = load_records("records_sample.txt")


# =============================================================== PROCESS + OUTPUT

for r in records:
    diff, percent, status = check_record(r["value"], r["limit"])
    print_report(r["label"], r["value"], r["limit"], diff, percent, status)

for r in records_from_file:
    diff, percent, status = check_record(r["value"], r["limit"])
    print_report(r["label"], r["value"], r["limit"], diff, percent, status)

over_count = 0
with open("results.txt", "w") as f:
    for r in records_for_results:
        diff, percent, status = check_record(r["value"], r["limit"])
        print_report(r["label"], r["value"], r["limit"], diff, percent, status)
        f.write(f"{r['label']},{status}\n")
        if status == "OVER LIMIT":
            over_count += 1

(f"Total OVER LIMIT records: {over_count}")

# Read results back
try:
    with open("results.txt") as f:
        print("\nContents of results.txt:")
        print(f.read())
except FileNotFoundError:
    print("results.txt not found.")





