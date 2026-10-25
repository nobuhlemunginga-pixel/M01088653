"""
RECORD CHECK  -  my version
===========================

Name  :Philippa Munginga
Lane  :  AI      (delete two)
Date  :25/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
class Record:
    over_limit_count = 0

    def __init__(self, dataset_name, rows_loaded, rows_expected):
        """Store dataset information."""
        self.dataset_name = dataset_name
        self.rows_loaded = rows_loaded
        self.rows_expected = rows_expected

    def status(self):
        """Return the dataset status."""
        percent = (self.rows_loaded / self.rows_expected) * 100

        if percent >= 100:
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"
        

# ==================================================================== RECORDS

def load_records(path):
    records = []
    
    with open(path, "r") as file:
        for line in file:
            dataset_name, rows_loaded, rows_expected = line.strip().split(",")

            records.append(Record(dataset_name, float(rows_loaded), float(rows_expected)))
        
    return records

records = load_records("records_sample.txt")


# ==================================================================== OUTPUT

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.dataset_name}")
    print("=" * 34)

    # your report lines go here
    print("Dataseet Name:", record.dataset_name)
    print("Rows Loaded:  ", record.rows_loaded)
    print("Rows Expected:", record.rows_expected)
    print("Status:       ", record.status())
    print("=" * 34)
    print()
    print("OVER LIMIT datasets:", Record.over_limit_count)


# ==========================================================================
