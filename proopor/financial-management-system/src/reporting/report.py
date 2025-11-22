def generate_excel_report(data, filename):
    import pandas as pd

    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)


def generate_pdf_summary(data, filename):
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.output(filename)


def create_action_recommendations(metrics):
    recommendations = []
    
    if metrics['profit_margin'] < 0.1:
        recommendations.append("Consider reducing costs or increasing prices.")
    if metrics['debt_to_equity'] > 1:
        recommendations.append("Evaluate debt levels and consider reducing liabilities.")
    
    return recommendations