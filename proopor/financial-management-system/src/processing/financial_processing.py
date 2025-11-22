def build_cashflow(data):
    cashflow = data.groupby('Date')['Amount'].sum().reset_index()
    return cashflow

def compute_dre(data):
    revenue = data[data['Type'] == 'Revenue']['Amount'].sum()
    expenses = data[data['Type'] == 'Expense']['Amount'].sum()
    dre = revenue - expenses
    return dre

def generate_cashflow_report(cashflow):
    report = {
        'Total Cashflow': cashflow['Amount'].sum(),
        'Average Daily Cashflow': cashflow['Amount'].mean(),
        'Cashflow Details': cashflow
    }
    return report