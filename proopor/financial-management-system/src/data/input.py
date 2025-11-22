def load_data(file_path):
    import pandas as pd
    
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")
    
    return data

def clean_data(data):
    # Remove any rows with missing values
    cleaned_data = data.dropna()
    return cleaned_data

def normalize_data(data):
    # Normalize numerical columns (example: scaling between 0 and 1)
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
    for col in numerical_cols:
        data[col] = (data[col] - data[col].min()) / (data[col].max() - data[col].min())
    return data