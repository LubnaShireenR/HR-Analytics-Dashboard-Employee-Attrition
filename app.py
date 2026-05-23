import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load dataset
df = pd.read_csv(r"C:\Users\lubna shireen\HR Analytics Dashboard – Employee Attrition Analysis\HR-Employee-Attrition.csv")

# Title
st.title("📊 HR Analytics Dashboard - Employee Attrition Analysis")
st.markdown("Interactive dashboard for workforce analytics and attrition insights.")

# Sidebar filters
st.sidebar.header("Filters")

department = st.sidebar.multiselect(
    "Department",
    df['Department'].unique(),
    default=df['Department'].unique()
)

gender = st.sidebar.multiselect(
    "Gender",
    df['Gender'].unique(),
    default=df['Gender'].unique()
)

overtime = st.sidebar.multiselect(
    "OverTime",
    df['OverTime'].unique(),
    default=df['OverTime'].unique()
)

# Filter data
filtered_df = df[
    (df['Department'].isin(department)) &
    (df['Gender'].isin(gender)) &
    (df['OverTime'].isin(overtime))
]

# KPI metrics
total_employees = filtered_df.shape[0]
attrition_count = filtered_df[filtered_df['Attrition'] == 'Yes'].shape[0]
attrition_rate = (attrition_count / total_employees) * 100
avg_income = filtered_df['MonthlyIncome'].mean()
avg_age = filtered_df['Age'].mean()
avg_years = filtered_df['YearsAtCompany'].mean()

# KPI cards
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

col1.metric("Employees", total_employees)
col2.metric("Attrition", attrition_count)
col3.metric("Attrition Rate", f"{attrition_rate:.2f}%")

col4.metric("Avg Income", f"${avg_income:,.0f}")
col5.metric("Avg Age", f"{avg_age:.1f}")
col6.metric("Avg Years", f"{avg_years:.1f}")

# Charts
st.subheader("Attrition by Department")
fig1 = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Attrition by Job Role")
fig2 = px.histogram(filtered_df, y="JobRole", color="Attrition")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Overtime Impact")
fig3 = px.histogram(filtered_df, x="OverTime", color="Attrition")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Gender-wise Attrition")
fig4 = px.histogram(filtered_df, x="Gender", color="Attrition")
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Monthly Income Distribution")
fig5 = px.histogram(filtered_df, x="MonthlyIncome")
st.plotly_chart(fig5, use_container_width=True)

st.subheader("Age Distribution")
fig6 = px.histogram(filtered_df, x="Age")
st.plotly_chart(fig6, use_container_width=True)

st.subheader("Job Satisfaction vs Attrition")
fig7 = px.histogram(filtered_df, x="JobSatisfaction", color="Attrition")
st.plotly_chart(fig7, use_container_width=True)