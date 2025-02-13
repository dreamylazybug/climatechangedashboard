import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data - daily chemical exposure
exposure_data = pd.DataFrame({
    'Time of Day': ['Morning', 'Morning', 'Afternoon', 'Afternoon', 'Evening', 'Evening'],
    'Chemical': ['Pesticides (Food)', 'Shampoo (Personal Care)', 'Air Fresheners (Air)', 'Detergents (Cleaning)', 'Processed Food Additives', 'Cosmetics (Personal Care)'],
    'Exposure Level (mg)': [5, 8, 6, 10, 12, 7]
})

# Streamlit UI
st.set_page_config(page_title="Daily Chemical Exposure Tracker", layout="wide")
st.title("Interactive Dashboard: Daily Chemical Exposure")

# Filter options
category = st.multiselect("Select Chemical Categories:", exposure_data['Chemical'].unique(), exposure_data['Chemical'].unique())

# Apply filter
df_filtered = exposure_data[exposure_data['Chemical'].isin(category)]

# Exposure breakdown visualization
fig_bar = px.bar(df_filtered, x='Time of Day', y='Exposure Level (mg)', color='Chemical', title="Chemical Exposure by Time of Day")
st.plotly_chart(fig_bar, use_container_width=True)

# Pie chart of chemical categories
fig_pie = px.pie(df_filtered, names='Chemical', values='Exposure Level (mg)', title="Chemical Exposure Distribution")
st.plotly_chart(fig_pie, use_container_width=True)

# Customization sliders
st.sidebar.header("Adjust Exposure Levels")
adjustments = {}
for chemical in exposure_data['Chemical'].unique():
    adjustments[chemical] = st.sidebar.slider(f"{chemical} (mg)", 0, 20, exposure_data[exposure_data['Chemical'] == chemical]['Exposure Level (mg)'].values[0])

# Update data with user inputs
for chemical, value in adjustments.items():
    exposure_data.loc[exposure_data['Chemical'] == chemical, 'Exposure Level (mg)'] = value

st.success("Adjust values to customize exposure analysis!")
