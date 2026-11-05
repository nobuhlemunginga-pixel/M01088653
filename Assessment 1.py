# Question 1(a)
# Load and explore climate data


import pandas as pd

#Load the CSV file into a pandas dataframe
climate_df = pd.read_csv("climate_data.csv")

# Keep only the required columns
selected_columns = [
    "geoAreaName",
    "timePeriodStart",
    "EG_FEC_RNEW",
    "EN_ATM_GHGT_WLU"
]

climate_df = climate_df[selected_columns]

# Display the first five rows
print("First 5 rows:")
print(climate_df.head())

# What type of data is in each column?
print("\nData Types:")
print(climate_df.dtypes)

#How much data is missing?
print("\nMissing Values Per Column:")
print(climate_df.isnull().sum())

print("\nTotal Missing Values:")
print(climate_df.isnull().sum().sum())

# Question 1(b)

# Renewable energy proportion in the UK in 2022

uk_2022 = climate_df[
    (climate_df["geoAreaName"] ==
     "United Kingdom of Great Britain and Northern Ireland")
     &
     (climate_df["timePeriodStart"] == 2022)
]

print("\nUK Renewable Energy Percentage (2022):")
print(uk_2022["EG_FEC_RNEW"])

# Greenhouse gas emissions in Mauritius in 2020

mauritius_2020 = climate_df[
    (climate_df["geoAreaName"] == "Mauritius")
    &
    (climate_df["timePeriodStart"] == 2020)
]

print("\nMauritius Greenhouse Gas Emissions (2020):")
print(mauritius_2020["EN_ATM_GHGT_WLU"])

# Country with highest renewable energy % in 2023

renewable_2023 = climate_df[
    climate_df["timePeriodStart"] == 2023
]

highest_country = renewable_2023.loc[
    renewable_2023["EG_FEC_RNEW"].idxmax()
]

print("\nCountry with Highest Renewable Energy Use in 2023:")
print("Country:", highest_country["geoAreaName"])
print("Percentage:", highest_country["EG_FEC_RNEW"])

# Question 1(c)

import matplotlib.pyplot as plt

# Histogram of renewable energy use in 2020

renewable_2020 = climate_df[
    climate_df["timePeriodStart"] == 2020
]

plt.figure(figsize=(8,5))
plt.hist(
    renewable_2020["EG_FEC_RNEW"].dropna(),
    bins=15,
    edgecolor="black"
)

plt.title("Distribution of Renewable Energy Use (2020)")
plt.xlabel("Renewable Energy Percentage")
plt.ylabel("Frequency")

plt.show()
# The Histogram shows the distribution of renewable energy consumption percentages across countries in 2020.
# Most countries appear to have relatively low to moderate percentages, while a smaller number have very high values, suggesting a positively skewed distribution.

# Top 10 greenhouse gas emitters in 2021

emissions_2021 = climate_df[
    climate_df["timePeriodStart"] == 2021
]

emissions_2021 = emissions_2021.dropna(
    subset=["EN_ATM_GHGT_WLU"]
)

top_10_emitters = emissions_2021.nlargest(
    10,
    "EN_ATM_GHGT_WLU"
)

plt.figure(figsize=(12,6))

plt.bar(
    top_10_emitters["geoAreaName"],
    top_10_emitters["EN_ATM_GHGT_WLU"],
    color="steelblue"
)

plt.title("Top 10 Greenhouse Gas Emitters (2021)")
plt.xlabel("Country")
plt.ylabel("Greenhouse Gas Emissions (Mt CO2E)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# The bar chart displays the ten countries with the highest greenhouse gas emissions in 2021.
# The highest emitting countries produce substantially more emmissions than others, indicating that global emissions are concentrated among a relatively small number of countries.

# Time Series of Renewable Energy Use

countries = [ 
    "United Kingdom of Great Britain and Northern Ireland",
    "Mauritius",
    "United Arab Emirates",
    "India",
    "Germany",
    "Brazil"
]

plt.figure(figsize=(12,6))

for country in countries:

    country_data = climate_df[
        climate_df["geoAreaName"] == country
    ]

    plt.plot(
        country_data["timePeriodStart"],
        country_data["EG_FEC_RNEW"],
        label=country
    )

plt.title("Renewable Energy Use Over Time")
plt.xlabel("Year")
plt.ylabel("Renewable Energy Percentage")

plt.legend()
plt.grid(True)

plt.show()
# The time series graph shows changes in renewable energy use over time for six countries.
# Most countries show an upward trend, suggesting an increasing adoption of renewable energy sources over the observed period.

# Question 1(d)

emissions = climate_df["EN_ATM_GHGT_WLU"].dropna()

print("Summary Statistics")
print("------------------")

print("Mean:", emissions.mean())
print("Median:", emissions.median())
print("Minimum:", emissions.min())
print("Maximum:", emissions.max())
print("Standard Deviation:", emissions.std())

print("First Quartile (Q1):", emissions.quantile(0.25))
print("Third Quartile (Q3):", emissions.quantile(0.75))

iqr = emissions.quantile(0.75) - emissions.quantile(0.25)

print("Interquartile Range (IQR):", iqr)

# The mean and median provide measures of the central tendency of greenhouse gas emissions. If the mean is noticeable larger than the median this suggests that the distribution is positively skewed by a small number of countries with very high emissions.
# The standard deviation measures how spread out the emissions values are around the mean. A large standard deviation would indicate substantial variation between countries.
# The interquartile range describes the spread of the middle 50% of the overall range helps identify whether outliers are present.
# Overall, greenhouse gas emissions are unlikely to be evenly distributed across countries, as a few countries typically contribute disproportionately high emission levels.
