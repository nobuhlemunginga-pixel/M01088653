"""
RECORD CHECK  -  my version
===========================

Name  : Philippa Munginga
Lane  :  AI      
Date  : 7/11/2026

Run it:   python template.py

"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Convert one messy line into a clean dictionary."""

    raw_line = raw_line.strip()

    dataset_part, rest = raw_line.split(",", 1)

    record = {
        "dataset": dataset_part.strip().lower()
    }

    for piece in rest.split(","):
        key, value = piece.split("=")

        key = key.strip().lower()
        value = float(value.strip())

        record[key] = value

    return record


def status_of(record):
    """Return the status for one dataset."""

    if record["rating"] >= 4:
        return "FLAGGED"
    else:
        return "OK"



# ====================================================================== INPUT

raw_records = []

with open("data_science_records.txt", "r") as file:
    for line in file:
        raw_records.append(line)


# =============================================================== PROCESS + OUTPUT

record_count = 0
flagged_count = 0

for raw_record in raw_records:

    record = parse_line(raw_record)

    status = status_of(record)
    
    print(record)
    print("Status:", status)
    print()

    record_count += 1

    if status == "FLAGGED":
        flagged_count += 1

print("Summary:")
print("Records =", record_count)
print("Flagged =", flagged_count)


# =========================================================================
