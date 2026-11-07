"""
RECORD CHECK  -  my version
===========================

Name  : Philippa
Lane  :  AI
Date  : 6/11/2026

Run it:   python template.py

"""

import pandas as pd
import matplotlib.pyplot as plt
# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv("data_science.csv") 


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100

df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK"
)

# ================================================================== OUTPUT
# 3. Print the DataFrame.
#

print("FULL DATAFRAME")
print(df)

# Show only rows that are not OK

print("\nROWS THAT ARE NOT OK")
print(df[df["status"] != "OK"])

#Group by status and count each group

print("\nCOUNT PER STATUS")
print(df.groupby("status").size())

# Save the completed Dataframe

df.to_csv("data_science_report.csv", index=False)

# Create and save a bar chart

df["status"].value_counts().plot(kind="bar")

plt.title("Dataset Status Counts")
plt.xlabel("Status")
plt.ylabel("Count")

plt.savefig("status_counts.png")
plt.show()


# ========================================================================
