# Energy Consumption EDA Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# 1. Load the Data
# ---------------------------
df = pd.read_csv("C:/Users/aarav/Downloads/global_energy_consumption.csv")

# ---------------------------
# 2. Data Cleaning
# ---------------------------

# Replace "\N" and similar placeholders with NaN
df.replace(r"\\N", np.nan, regex=True, inplace=True)
df.dropna(inplace=True)

# Fix column names: strip, replace spaces with underscores, remove brackets
df.columns = (
    df.columns.str.strip()
    .str.replace(' ', '_')
    .str.replace('(', '')
    .str.replace(')', '')
    .str.replace('/', '_')
)

# Convert object types to float where applicable
for col in df.columns:
    if df[col].dtype == 'object':
        try:
            df[col] = df[col].astype(float)
        except:
            pass

df.drop_duplicates(inplace=True)

# ---------------------------
# 3. Descriptive Statistics
# ---------------------------

print("\n--- Cleaned Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

# ---------------------------
# 4. EDA & Visualizations
# ---------------------------
sns.set(style="whitegrid", palette="Set2")

# 1. Line Plot - Average Energy Consumption Over Years
plt.figure(figsize=(10, 6))
yearly_energy = df.groupby("Year")["Total_Energy_Consumption_TWh"].mean()
sns.lineplot(x=yearly_energy.index, y=yearly_energy.values, marker="o")
plt.title("Average Energy Consumption Over Years")
plt.xlabel("Year")
plt.ylabel("Avg. Consumption (TWh)")
plt.show()

# 2. Bar Plot - Top 10 Countries by Total Energy Consumption
plt.figure(figsize=(10, 6))
top_countries = df.groupby("Country")["Total_Energy_Consumption_TWh"].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 10 Countries by Total Energy Consumption")
plt.xlabel("Total Consumption (TWh)")
plt.ylabel("Country")
plt.show()

# 3. Histogram - Renewable Energy Share Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["Renewable_Energy_Share_%"], bins=20, kde=True, color="skyblue")
plt.title("Distribution of Renewable Energy Share")
plt.xlabel("Renewable Energy Share (%)")
plt.show()

# 4. Scatter Plot - Fossil Fuel Dependency vs Renewable Share
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Renewable_Energy_Share_%", y="Fossil_Fuel_Dependency_%", data=df, alpha=0.6)
plt.title("Fossil Fuel vs Renewable Energy Share")
plt.xlabel("Renewable Energy Share (%)")
plt.ylabel("Fossil Fuel Dependency (%)")
plt.show()

# 5. Line Plot - Global Carbon Emissions Over Time
plt.figure(figsize=(10, 6))
carbon = df.groupby("Year")["Carbon_Emissions_Million_Tons"].sum()
sns.lineplot(x=carbon.index, y=carbon.values, color="salmon", marker="o")
plt.title("Global Carbon Emissions Over Time")
plt.xlabel("Year")
plt.ylabel("Emissions (Million Tons)")
plt.show()

# 6. Scatter Plot - Per Capita Energy Use vs Carbon Emissions
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Per_Capita_Energy_Use_kWh", y="Carbon_Emissions_Million_Tons", color="purple")
plt.title("Per Capita Energy Use vs Carbon Emissions")
plt.xlabel("Per Capita Energy Use (kWh)")
plt.ylabel("Carbon Emissions (Million Tons)")
plt.show()

# 7. Heatmap - Correlation of Numeric Features
plt.figure(figsize=(12, 8))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap of Numerical Features")
plt.show()

# 8. Boxplot - Energy Price Distribution
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Energy_Price_Index_USD_kWh", color="lightgreen")
plt.title("Distribution of Energy Prices")
plt.xlabel("Energy Price (USD/kWh)")
plt.show()

# 9. Pie Chart - Energy Price Categories
plt.figure(figsize=(8, 8))
price_bins = pd.cut(df["Energy_Price_Index_USD_kWh"], bins=[0, 0.10, 0.20, 0.30, df["Energy_Price_Index_USD_kWh"].max()],
                    labels=["0-0.10", "0.10-0.20", "0.20-0.30", ">0.30"])
price_dist = price_bins.value_counts().sort_index()
colors = sns.color_palette("pastel")
plt.pie(price_dist.values, labels=price_dist.index, colors=colors, autopct='%1.1f%%')
plt.title("Energy Price Distribution Categories")
plt.axis('equal')
plt.show()
# ---------------------------
# 5. Summary & Additional Insights
# ---------------------------
total_energy = df["Total_Energy_Consumption_TWh"].sum()
print(f"\n🌍 Total Global Energy Consumed in Dataset: {total_energy:.2f} TWh")

fossil_dependent = df[df["Fossil_Fuel_Dependency_%"] > 90]["Country"].nunique()
print(f"⚠️ Countries highly dependent on fossil fuels (>90%): {fossil_dependent}")

renewable_leaders = df[df["Renewable_Energy_Share_%"] > 75]["Country"].nunique()
print(f"💡 Countries with >75% renewable energy: {renewable_leaders}")

high_price = df[df["Energy_Price_Index_USD_kWh"] > 0.30]["Country"].value_counts()
print(f"\n💰 Countries with high energy prices (>0.30 USD/kWh):\n{high_price.head()}")
