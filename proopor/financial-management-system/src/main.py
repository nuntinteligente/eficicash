# filepath: financial-management-system/src/main.py

import streamlit as st
from data.input import load_data, clean_data
from processing.financial_processing import build_cashflow, generate_cashflow_report
from analysis.metrics import compute_metrics
from visualization.plots import create_cashflow_plot
from reporting.report import generate_excel_report

def main():
    st.title("Financial Management System")
    
    st.sidebar.header("Upload Data")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        cleaned_data = clean_data(data)
        
        st.subheader("Cleaned Data")
        st.write(cleaned_data)
        
        cashflow = build_cashflow(cleaned_data)
        st.subheader("Cashflow")
        st.write(cashflow)
        
        metrics = compute_metrics(cashflow)
        st.subheader("Financial Metrics")
        st.write(metrics)
        
        st.subheader("Cashflow Plot")
        create_cashflow_plot(cashflow)
        
        if st.button("Generate Cashflow Report"):
            report = generate_cashflow_report(cashflow)
            st.download_button("Download Report", report, "cashflow_report.pdf")
        
        if st.button("Generate Excel Report"):
            excel_report = generate_excel_report(cleaned_data)
            st.download_button("Download Excel Report", excel_report, "financial_report.xlsx")

if __name__ == "__main__":
    main()