# Global-energy-consumption-EDA
# 🌍 Energy Consumption EDA Project

## 📜 Project Overview
This project delves into the analysis of global energy consumption trends, patterns, and correlations using a dataset of energy statistics. It employs exploratory data analysis (EDA) techniques to uncover key insights into energy usage, carbon emissions, renewable energy adoption, and pricing trends globally.

## 📁 Dataset Information
- **File**: `global_energy_consumption.csv`
- **Key Features**:
  - `Year`: The year of observation.
  - `Country`: The name of the country.
  - `Total_Energy_Consumption_TWh`: Total energy consumed in terawatt-hours.
  - `Renewable_Energy_Share_%`: Percentage share of renewable energy.
  - `Fossil_Fuel_Dependency_%`: Percentage dependency on fossil fuels.
  - `Carbon_Emissions_Million_Tons`: Carbon emissions in million tons.
  - `Per_Capita_Energy_Use_kWh`: Energy usage per person in kilowatt-hours.
  - `Energy_Price_Index_USD_kWh`: Energy price in USD per kilowatt-hour.

## 🔧 Steps Followed

### 1️⃣ Data Loading
- Loaded the dataset using pandas into a DataFrame.

### 2️⃣ Data Cleaning
- Replaced placeholder values (e.g., `"\N"`) with NaN and dropped rows with missing data.
- Renamed columns to be consistent (e.g., spaces replaced with underscores, unnecessary characters removed).
- Converted applicable columns to numeric types.
- Removed duplicate rows for better accuracy.

### 3️⃣ Descriptive Statistics
- Used `info()` and `describe()` to analyze the dataset structure and summarize statistical properties.

### 4️⃣ Exploratory Data Analysis (EDA)
Created the following visualizations to understand energy-related trends:
1. **Line Plot**:
   - Tracked the average energy consumption over years.
2. **Bar Plot**:
   - Highlighted the top 10 countries by total energy consumption.
3. **Histogram**:
   - Displayed the distribution of renewable energy share (%) among countries.
4. **Scatter Plot**:
   - Compared fossil fuel dependency (%) with renewable energy share (%).
5. **Line Plot**:
   - Visualized global carbon emissions trends over time.
6. **Scatter Plot**:
   - Explored the relationship between per capita energy use and carbon emissions.
7. **Heatmap**:
   - Showed correlations between numerical features.
8. **Boxplot**:
   - Represented the distribution of energy prices globally.
9. **Pie Chart**:
   - Categorized countries into energy price ranges.

### 5️⃣ Key Insights
- **Total Global Energy Consumption**: Derived total energy consumed in TWh.
- **Fossil Fuel Dependency**: Counted countries with more than 90% reliance on fossil fuels.
- **Renewable Leaders**: Identified countries with >75% renewable energy usage.
- **High Energy Prices**: Highlighted countries with energy prices above 0.30 USD/kWh.

## 📊 Tools & Libraries
- **Python**: Core programming language.
- **Pandas**: Data cleaning and manipulation.
- **NumPy**: Numerical computations.
- **Matplotlib**: Data visualization.
- **Seaborn**: Enhanced data visualization.

## 🚀 How to Run
1. Ensure Python is installed (preferably version 3.8 or higher).
2. Install the required libraries using `pip install pandas numpy matplotlib seaborn`.
3. Load your dataset at the specified path (`global_energy_consumption.csv`).
4. Run the script to generate EDA results and visualizations.

## 🔮 Future Enhancements
- Perform advanced statistical modeling or machine learning predictions.
- Expand analysis by adding more external datasets.
- Develop an interactive dashboard for dynamic visualizations.

## 📬 Feedback
Feel free to reach out if you have questions or need further assistance with this project!

---

Happy viva preparation! Let me know if you'd like to modify or expand any section. 😊
