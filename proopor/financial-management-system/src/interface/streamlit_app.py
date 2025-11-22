import streamlit as st
import pandas as pd
from src.data.input import load_data, clean_data
from src.processing.financial_processing import build_cashflow, generate_cashflow_report
from src.analysis.metrics import compute_metrics
from src.visualization.plots import create_cashflow_plot, create_revenue_expense_bar
from src.reporting.report import generate_excel_report

def main():
    st.title("Financial Management System")

    st.sidebar.header("Upload Data")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            data = load_data(uploaded_file)
        else:
            data = load_data(uploaded_file, file_type='excel')

        cleaned_data = clean_data(data)
        st.write("Cleaned Data", cleaned_data)

        if st.sidebar.button("Generate Cashflow Report"):
            cashflow = build_cashflow(cleaned_data)
            report = generate_cashflow_report(cashflow)
            st.write("Cashflow Report", report)

            st.sidebar.download_button("Download Report", report, file_name="cashflow_report.xlsx")

        if st.sidebar.button("Show Metrics"):
            metrics = compute_metrics(cleaned_data)
            st.write("Financial Metrics", metrics)

        if st.sidebar.button("Visualize Cashflow"):
            create_cashflow_plot(cleaned_data)
            st.pyplot()

        if st.sidebar.button("Revenue vs Expense"):
            create_revenue_expense_bar(cleaned_data)
            st.pyplot()

if __name__ == "__main__":
    main()