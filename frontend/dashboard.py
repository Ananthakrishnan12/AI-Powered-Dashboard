import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.express as px

from backend.crew import run_ai_analysics

st.set_page_config(page_title="AI Dashboard Generator", layout="wide")

st.title("📊 AI Dashboard Generator")

file = st.file_uploader("Upload CSV Dataset", type=["csv"])

if file:

    df = pd.read_csv(file)

    # ===============================
    # Dataset Overview
    # ===============================
    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    st.divider()

    # ===============================
    # Data Table
    # ===============================
    st.subheader("Dataset Preview")
    st.dataframe(df, use_container_width=True)

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    cat_cols = df.select_dtypes(include=['object']).columns

    # ===============================
    # Charts Section
    # ===============================
    if len(cat_cols) > 0 and len(numeric_cols) > 0:

        x = cat_cols[0]
        y = numeric_cols[0]

        st.subheader("Visualizations")

        col1, col2 = st.columns(2)

        # Bar Chart
        with col1:
            st.markdown("### Bar Chart")
            fig = px.bar(df, x=x, y=y)
            st.plotly_chart(fig, use_container_width=True)

        # Pie Chart
        with col2:
            st.markdown("### Pie Chart")
            fig2 = px.pie(df, names=x, values=y)
            st.plotly_chart(fig2, use_container_width=True)

        col3, col4 = st.columns(2)

        # Scatter Plot
        with col3:
            st.markdown("### Scatter Plot")
            fig3 = px.scatter(df, x=x, y=y)
            st.plotly_chart(fig3, use_container_width=True)

        # Histogram
        with col4:
            st.markdown("### Histogram")
            fig4 = px.histogram(df, x=y)
            st.plotly_chart(fig4, use_container_width=True)

    st.divider()

    # ===============================
    # Summary Table
    # ===============================
    st.subheader("Statistical Summary")
    st.dataframe(df.describe(), use_container_width=True)

    st.divider()

    # ===============================
    # AI Insights Section
    # ===============================
    st.subheader("AI Insights")

    if st.button("Generate AI Insights"):

        insights = run_ai_analysis()

        st.success("AI Analysis Completed")

        st.write(insights)