import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

st.title("📊 Narrowband Signal Visualizations")

# Load the narrowband signals data
data = pd.read_csv("narrowband_signals.csv")

# Display the dataset
st.write("### Dataset Overview")
st.dataframe(data.head())

# ---- Bar Plot ----
st.write("### Bar Plot")
barplot_columns = st.multiselect(
    "Choose one feature to visualize on Y-axis for the Bar Plot and 'Stars Type' will be on X-axis:",
    ['brightpixel', 'narrowband', 'narrowbanddrd', 'noise', 'Signal Frequency(MHz)', 'Signal Duration(seconds)'],
    default=['brightpixel']
)

if len(barplot_columns) == 1:
    st.write(f"### Bar Plot of {barplot_columns[0]}")
    fig, ax = plt.subplots()
    sns.barplot(x='Stars Type', y=barplot_columns[0], data=data, ax=ax)
    st.pyplot(fig)
else:
    st.error("Please select exactly 1 feature for the Bar Plot.")

# ---- Correlation Heatmap ----
st.write("### Correlation Heatmap")
heatmap_columns = st.multiselect(
    "Choose at least 2 features for the Correlation Heatmap:",
    ['brightpixel', 'narrowband', 'narrowbanddrd', 'noise', 'Signal Frequency(MHz)', 'Signal Duration(seconds)'],
    default=['brightpixel', 'narrowband']
)

if len(heatmap_columns) >= 2:
    st.write(f"### Correlation Heatmap for {', '.join(heatmap_columns)}")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(data[heatmap_columns].corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
else:
    st.error("Please select at least 2 features for the Correlation Heatmap.")

# ---- Scatter Plot: Signal Frequency vs Signal Duration ----
st.write("### Scatter Plot: Signal Frequency vs Signal Duration")
scatter_columns = st.multiselect(
    "Choose 2 columns for X and Y axes:",
    ['Signal Frequency(MHz)', 'Signal Duration(seconds)'],
    default=['Signal Frequency(MHz)', 'Signal Duration(seconds)']
)

if len(scatter_columns) == 2:
    st.write(f"### Scatter Plot: {scatter_columns[0]} vs {scatter_columns[1]}")
    fig, ax = plt.subplots()
    sns.scatterplot(x=scatter_columns[0], y=scatter_columns[1], hue='Stars Type', data=data, ax=ax)
    st.pyplot(fig)
else:
    st.error("Please select exactly 2 columns for the Scatter Plot.")

# ---- Sunburst Plot 1 ----
st.write("### Sunburst Plot 1")
sunburst_columns_1 = st.multiselect(
    "Choose at least 2 columns for Sunburst Plot 1:",
    ['Stars Type', 'brightpixel', 'narrowband', 'narrowbanddrd', 'noise', 'Signal Frequency(MHz)', 'Signal Duration(seconds)', 'Remarks'],
    default=['Stars Type', 'Remarks']
)

if len(sunburst_columns_1) >= 2:
    fig_sunburst_1 = px.sunburst(data, path=sunburst_columns_1)
    st.plotly_chart(fig_sunburst_1)
else:
    st.error("Please select at least 2 columns for Sunburst Plot 1.")

# ---- Sunburst Plot 2 ----
st.write("### Sunburst Plot 2")
sunburst_columns_2 = st.multiselect(
    "Choose at least 2 columns for Sunburst Plot 2:",
    ['Stars Type', 'brightpixel', 'narrowband', 'narrowbanddrd', 'noise', 'Signal Frequency(MHz)', 'Signal Duration(seconds)', 'Remarks'],
    default=['Stars Type', 'Signal Frequency(MHz)']
)

if len(sunburst_columns_2) >= 2:
    fig_sunburst_2 = px.sunburst(data, path=sunburst_columns_2)
    st.plotly_chart(fig_sunburst_2)
else:
    st.error("Please select at least 2 columns for Sunburst Plot 2.")

# ---- Sunburst Plot 3 ----
st.write("### Sunburst Plot 3")
sunburst_columns_3 = st.multiselect(
    "Choose at least 2 columns for Sunburst Plot 3:",
    ['Stars Type', 'brightpixel', 'narrowband', 'narrowbanddrd', 'noise', 'Signal Frequency(MHz)', 'Signal Duration(seconds)', 'Remarks'],
    default=['Stars Type', 'narrowband']
)

if len(sunburst_columns_3) >= 2:
    fig_sunburst_3 = px.sunburst(data, path=sunburst_columns_3)
    st.plotly_chart(fig_sunburst_3)
else:
    st.error("Please select at least 2 columns for Sunburst Plot 3.")

# ---- Boxplot ----
st.write("### Boxplot of Brightpixel vs. Stars Type")
fig, ax = plt.subplots()
sns.boxplot(x='Stars Type', y='brightpixel', data=data, ax=ax)
st.pyplot(fig)

# ---- Violin Plot ----
st.write("### Violin Plot of Narrowband vs. Stars Type")
fig, ax = plt.subplots()
sns.violinplot(x='Stars Type', y='narrowband', data=data, ax=ax)
st.pyplot(fig)

# ---- Pairplot ----
st.write("### Pairplot of Selected Features")
pairplot_columns = st.multiselect(
    "Choose features for Pairplot (at least 2):",
    ['brightpixel', 'narrowband', 'narrowbanddrd', 'noise', 'Signal Frequency(MHz)', 'Signal Duration(seconds)', 'Stars Type'],
    default=['brightpixel', 'narrowband', 'narrowbanddrd', 'noise']
)

if len(pairplot_columns) >= 2:
    fig = sns.pairplot(data[pairplot_columns], hue='Stars Type')
    st.pyplot(fig)
else:
    st.error("Please select at least 2 features for the Pairplot.")

# ---- Histogram ----
st.write("### Histogram of Signal Frequency (MHz)")
fig, ax = plt.subplots()
sns.histplot(data['Signal Frequency(MHz)'], bins=20, kde=True, ax=ax)
st.pyplot(fig)

# ---- Line Plot ----
st.write("### Line Plot: Signal Frequency vs. Signal Duration")
fig, ax = plt.subplots()
sns.lineplot(x='Signal Duration(seconds)', y='Signal Frequency(MHz)', data=data, ax=ax)
st.pyplot(fig)

# ---- Heatmap ----
st.write("### Heatmap of Signal Frequency and Signal Duration (Brightness Intensity)")
fig, ax = plt.subplots()
sns.heatmap(data.pivot_table(values='brightpixel', index='Signal Frequency(MHz)', columns='Signal Duration(seconds)'), cmap="Blues", ax=ax)
st.pyplot(fig)

# ---- KDE Plot ----
st.write("### KDE Plot of Narrowband vs Narrowbanddrd")
fig, ax = plt.subplots()
sns.kdeplot(x='narrowband', y='narrowbanddrd', data=data, ax=ax, cmap="Reds", shade=True)
st.pyplot(fig)

# ---- Swarm Plot ----
st.write("### Swarm Plot of Noise vs. Stars Type")
fig, ax = plt.subplots()
sns.swarmplot(x='Stars Type', y='noise', data=data, ax=ax)
st.pyplot(fig)

# ---- Strip Plot ----
st.write("### Strip Plot of Signal Frequency(MHz) vs. Stars Type")
fig, ax = plt.subplots()
sns.stripplot(x='Stars Type', y='Signal Frequency(MHz)', data=data, ax=ax)
st.pyplot(fig)

# ---- Joint Plot ----
st.write("### Joint Plot of Brightpixel vs. Noise")
fig = sns.jointplot(x='brightpixel', y='noise', data=data, kind="hex", color="g")
st.pyplot(fig)
