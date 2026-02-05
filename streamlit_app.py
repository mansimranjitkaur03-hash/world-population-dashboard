import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("🌍 World Population Dashboard")

# Load dataset
df = pd.read_csv("world_population.csv")

st.subheader("📌 Dataset Preview")
st.write(df.head())

# Sidebar filters
st.sidebar.header("Filters")

continent = st.sidebar.selectbox("Select Continent", ["All"] + list(df["Continent"].unique()))

if continent != "All":
    df_filtered = df[df["Continent"] == continent]
else:
    df_filtered = df

st.subheader("📍 Filtered Data")
st.write(df_filtered)

# -------------------------------
# 1. Top 10 Most Populated Countries
# -------------------------------
st.subheader("🏆 Top 10 Most Populated Countries (2022)")

top10 = df_filtered.sort_values("2022 Population", ascending=False).head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x="2022 Population", y="Country/Territory", data=top10)
plt.title("Top 10 Most Populated Countries (2022)")
st.pyplot(plt)

# -------------------------------
# 2. Population Share by Continent
# -------------------------------
st.subheader("🌎 Total Population by Continent (2022)")

continent_pop = df.groupby("Continent")["2022 Population"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
continent_pop.plot(kind="bar")
plt.title("Total Population by Continent (2022)")
plt.ylabel("Population")
plt.xticks(rotation=45)
st.pyplot(plt)

# -------------------------------
# 3. Pie Chart - Continent Share
# -------------------------------
st.subheader("🥧 Population Share by Continent (Pie Chart)")

plt.figure(figsize=(7, 7))
continent_pop.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Population Share by Continent (2022)")
st.pyplot(plt)

# -------------------------------
# 4. Top 10 Most Dense Countries
# -------------------------------
st.subheader("🏙️ Top 10 Most Densely Populated Countries")

dense10 = df_filtered.sort_values("Density (per km²)", ascending=False).head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x="Density (per km²)", y="Country/Territory", data=dense10)
plt.title("Top 10 Most Densely Populated Countries")
st.pyplot(plt)

# -------------------------------
# 5. Scatter Plot: Area vs Population
# -------------------------------
st.subheader("📊 Relationship: Area vs Population (2022)")

plt.figure(figsize=(10, 6))
sns.scatterplot(x="Area (km²)", y="2022 Population", data=df_filtered)
plt.title("Area vs Population (2022)")
st.pyplot(plt)

# -------------------------------
# 6. Growth Analysis: 2000 vs 2022
# -------------------------------
st.subheader("📈 Population Growth (2000 → 2022)")

df_filtered["Growth_2000_2022"] = df_filtered["2022 Population"] - df_filtered["2000 Population"]

growth10 = df_filtered.sort_values("Growth_2000_2022", ascending=False).head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x="Growth_2000_2022", y="Country/Territory", data=growth10)
plt.title("Top 10 Countries with Highest Growth (2000-2022)")
st.pyplot(plt)

# -------------------------------
# 7. Heatmap Correlation
# -------------------------------
st.subheader("🔥 Correlation Heatmap (Numeric Columns)")

numeric_cols = df_filtered.select_dtypes(include=["float64", "int64"])

plt.figure(figsize=(12, 7))
sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
st.pyplot(plt)

# -------------------------------
# 8. Boxplot - Growth Rate by Continent
# -------------------------------
st.subheader("📦 Growth Rate Distribution by Continent")

plt.figure(figsize=(10, 6))
sns.boxplot(x="Continent", y="Growth Rate", data=df)
plt.xticks(rotation=45)
plt.title("Growth Rate Distribution by Continent")
st.pyplot(plt)

# -------------------------------
# Summary Insights
# -------------------------------
st.subheader("✅ Key Insights Summary")

st.write("""
- Asia contributes the highest population globally.
- Countries like China and India dominate the population ranking.
- Some smaller countries have extremely high population density.
- Population growth from 2000 to 2022 is highest in developing regions.
- Correlation heatmap shows strong relationships between population years.
- Growth rate distribution varies significantly across continents.
""")
