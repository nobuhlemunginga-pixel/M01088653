"""
RECORD CHECK  -  my version
===========================

Name  : Philippa Munginga
Lane  :  AI     
Date  : 20/10/2026

Run it:   python template.py

"""

# ==================================================================== INPUT
# 1. Ask the user for your three values

label = input("Dataset name: ")  
first = float(input("Rows loaded: "))   
second = float(input("Rows expected: "))   


# ================================================================== PROCESS
# 2. Work out what you were NOT given.     

difference = second - first # rows missing
percent = (first / second) * 100    # percent loaded
percent_missing = (difference / second) * 100 #percentage of rows that are missing from the dataset


# =================================================================== OUTPUT
# 3. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"{'Rows loaded':<15}: {first:>10.2f}")
print(f"{'Rows expected':<15}: {second:>10.2f}")
print(f"{'Rows missing':<15}: {difference:+10.2f}")
print(f"{'Loaded %':<15}: {percent:>10.2f}")
print(f"{'Missing %':<15}: {percent_missing:>10.2f}")
print("=" * 34)


# =========================================================================
