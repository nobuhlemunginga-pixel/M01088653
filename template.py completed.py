"""
RECORD CHECK  -  my version
===========================

Name  : Philippa Munginga
Lane  :  AI     
Date  : 10/10/2026

Run it:   python template.py

"""

# =================================================================== FUNCTIONS


def status_of(percent):
    """Return status string based on percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Return difference and percetage for value vs limit."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    """Print a bordered report with all details"""
    print()
    print("-" * 34)
    print(f" RECORD CHECK  -  {label}")
    print("-" * 34)
    print(f"{'Loaded' :10} : {value:8.2f}")
    print(f"{'Expected':10} : {limit:8.2f}")
    print(f"{'Diff':10} : {difference:+8.2f}")
    print(f"{'Percent':10} : {percent:8.2f} %")
    print(f"{'Status':10} : {status}")
    print("-" * 34)




# ==================================================================== INPUT

over_count = 0

while True:
    label = input("Enter dataset name (or 'quit' to stop): ")
    if label.lower() == "quit":
        break

    value = float(input("Enter rows loaded: "))
    limit = float(input("Enter rows expected: "))


# ================================================================== PROCESS
difference, percent = check(value, limit)
status = status_of(percent)


# =================================================================== OUTPUT

print_report(label, value, limit, difference, percent, status)

if status == "OVER LIMIT":
    over_count += 1


# ==========================================================================
