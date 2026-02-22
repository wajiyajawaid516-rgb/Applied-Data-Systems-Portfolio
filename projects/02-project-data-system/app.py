import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px

# Configuration
st.set_page_config(page_title="Project Data Management System", layout="wide")

st.title("🏗️ Digital Transformation: Project Management & Analytics")
st.markdown("""
### Transforming Fragmented Operational Data into Analytics-Ready Systems
*An architectural showcase of the system built for **Lee Wakemans**.*
""")

# Sidebar for Demo controls
st.sidebar.header("System Controls")
view_mode = st.sidebar.selectbox("Choose View", ["Executive Dashboard", "Relational Database Explorer", "Data Governance Tracker"])

# Mock Data for Showcase
@st.cache_data
def get_mock_data():
    projects = pd.DataFrame({
        'ProjectID': [101, 102, 103, 104],
        'Name': ['Infrastructure Alpha', 'Cloud Migration', 'Sustainability Audit', 'Digital HQ'],
        'Status': ['Active', 'Completed', 'Active', 'On Hold'],
        'Budget': [500000, 1200000, 300000, 850000],
        'Efficiency_Gain': [15, 45, 12, 0]
    })
    return projects

df = get_mock_data()

if view_mode == "Executive Dashboard":
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Projects", "10+", "+2 this month")
    col2.metric("Spreadsheet Reduction", "70%", "Goal: 90%")
    col3.metric("Secure Users", "15+", "Role-based access")
    
    st.markdown("### Budget vs Efficiency Gain")
    fig = px.bar(df, x='Name', y='Budget', color='Efficiency_Gain', barmode='group')
    st.plotly_chart(fig, use_container_width=True)

elif view_mode == "Relational Database Explorer":
    st.subheader("SQL/DuckDB Query Simulation")
    query = st.text_area("SQL Editor", "SELECT Name, Status, Budget FROM projects WHERE Status = 'Active'")
    if st.button("Run Query"):
        # Simulate DuckDB execution
        st.write("Results from DuckDB:")
        st.dataframe(df[df['Status'] == 'Active'][['Name', 'Status', 'Budget']])
        st.success("Query executed in 0.002s")

elif view_mode == "Data Governance Tracker":
    st.subheader("Access Controls & Lifecycle Management")
    st.info("System implements Field-Level Security and Automated Backups.")
    st.table(pd.DataFrame({
        'Feature': ['Encrypted Storage', 'Role-Based Access', 'Data Lineage', 'Audit Logs'],
        'Status': ['✅ Active', '✅ Active', '✅ Active', '✅ Active']
    }))

st.divider()
st.caption("Developed by Wajiya Anam Jawaid | Built with Python, FastAPI, Streamlit, and DuckDB.")
