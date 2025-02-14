import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data - daily chemical exposure
exposure_data = pd.read_csv("basic.csv")

# Streamlit UI
st.set_page_config(page_title="Take charge of your chemical exposure", layout="wide")
st.title("What's my Chemical Exposure today?")

# Filter options
category = st.sidebar.multiselect("Select a product that you use:", exposure_data['Consumer Product'].unique(), exposure_data['Consumer Product'].unique())
hzd = st.sidebar.multiselect("Select a health condition to see the chemicals & products to avoid:", ["Hormonal Imbalance/PCOD/Diabetes", "Respiratory Issues", "Liver Issues", "Skin Irritation", "Cancer", "Reproductive Issues", "Neurological Issues", "Immune System issues","Other Allergies"])

# Apply filter
df_filtered = exposure_data[exposure_data['Consumer Product'].isin(category)]
dff = df_filtered[['Product','Chemical','Health Hazards']]

# Exposure breakdown visualization
st.write("Ensure that the selected product does not have the following chemicals in ingredient list.")
st.divider()  # 👈 Draws a horizontal rule
st.dataframe(dff)
st.divider()  # 👈 Another horizontal rule

# Pie chart of chemical categories
if hzd == "Hormonal Imbalance/PCOD/Diabetes":
    dfs_filtered = exposure_data[exposure_data['Hormone Impact (PCOD/Diabetes/Thyroid)'] == 'Y']
    dfs = dfs_filtered[['Product','Chemical','Health Hazards']]
elif hzd == "Neurological Issues":
    dfg_filtered = exposure_data[exposure_data['Neurological Impact'] == 'Y']
    dfg = dfg_filtered[['Product','Chemical','Health Hazards']]
elif hzd == "Skin Irritation":
    dfg_filtered = exposure_data[exposure_data['Skin Allergies & Irritation'] == 'Y']
    dfg = dfg_filtered[['Product','Chemical','Health Hazards']]
elif hzd == "Cancer":
    dfg_filtered = exposure_data[exposure_data['Cancer Impact'] == 'Y']
    dfg = dfg_filtered[['Product','Chemical','Health Hazards']]
elif hzd == "Reproductive Issues":
    dfg_filtered = exposure_data[exposure_data['Reproduction Impact'] == 'Y']
    dfg = dfg_filtered[['Product','Chemical','Health Hazards']]
elif hzd == "Immune System issues":
    dfg_filtered = exposure_data[exposure_data['Immune System Impact'] == 'Y']
    dfg = dfg_filtered[['Product','Chemical','Health Hazards']]
elif hzd == "Respiratory Issues":
    dfg_filtered = exposure_data[exposure_data['Respiratory Impact'] == 'Y']
    dfg = dfg_filtered[['Product','Chemical','Health Hazards']]
elif hzd == "Liver Issues":
    dfg_filtered = exposure_data[exposure_data['Liver Damage'] == 'Y']
    dfg = dfg_filtered[['Product','Chemical','Health Hazards']]
elif hzd == "Other Allergies":
    dfg_filtered = exposure_data[exposure_data['Other Allergies'] == 'Y']
    dfg = dfg_filtered[['Product','Chemical','Health Hazards']]
else:
    print("Select a health condition.")

# Exposure breakdown visualization
st.write("For the health condition selected, ensure that the following products & chemicals are avoided.")
st.divider()  # 👈 Draws a horizontal rule
st.dataframe(dff)
st.divider()  # 👈 Another horizontal rule
