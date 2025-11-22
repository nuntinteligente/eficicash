def compute_metrics(financial_data):
    total_income = financial_data['Income'].sum()
    total_expenses = financial_data['Expenses'].sum()
    net_profit = total_income - total_expenses
    profit_margin = (net_profit / total_income) * 100 if total_income > 0 else 0

    metrics = {
        'Total Income': total_income,
        'Total Expenses': total_expenses,
        'Net Profit': net_profit,
        'Profit Margin (%)': profit_margin
    }
    
    return metrics

def detect_expense_impact(financial_data, threshold):
    high_expenses = financial_data[financial_data['Expenses'] > threshold]
    return high_expenses[['Date', 'Expenses']] if not high_expenses.empty else None