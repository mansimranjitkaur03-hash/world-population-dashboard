import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("World Population Dashboard")

# Load dataset
df = pd.read_csv("world_population.csv")

st.subheader("Dataset Preview")
st.write(df.head())

# Sidebar filter
st.sidebar.header("Filters")
continent = st.sidebar.selectbox("Select Continent", ["All"] + list(df["Continent"].unique()))

if continent != "All":
    df_filtered = df[df["Continent"] == continent]
else:
    df_filtered = df

st.subheader("Filtered Data")
st.write(df_filtered)

# Top 10 populated countries
st.subheader("Top 10 Most Populated Countries (2022)")

top10 = df_filtered.sort_values("2022 Population", ascending=False).head(10)

plt.figure()
sns.barplot(x="2022 Population", y="Country/Territory", data=top10)
plt.title("Top 10 Most Populated Countries")
st.pyplot(plt)
