def create_cashflow_plot(cashflow_data):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(cashflow_data['Date'], cashflow_data['Cashflow'], marker='o')
    plt.title('Cashflow Over Time')
    plt.xlabel('Date')
    plt.ylabel('Cashflow')
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def create_revenue_expense_bar(revenue_data, expense_data):
    import matplotlib.pyplot as plt
    import numpy as np

    categories = revenue_data['Category'].tolist()
    revenue_values = revenue_data['Amount'].tolist()
    expense_values = expense_data['Amount'].tolist()

    x = np.arange(len(categories))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    bars1 = ax.bar(x - width/2, revenue_values, width, label='Revenue')
    bars2 = ax.bar(x + width/2, expense_values, width, label='Expense')

    ax.set_xlabel('Categories')
    ax.set_ylabel('Amount')
    ax.set_title('Revenue and Expense by Category')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    plt.tight_layout()
    plt.show()

def create_category_donut(category_data):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 8))
    plt.pie(category_data['Amount'], labels=category_data['Category'], autopct='%1.1f%%', startangle=140)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title('Expense Distribution by Category')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()