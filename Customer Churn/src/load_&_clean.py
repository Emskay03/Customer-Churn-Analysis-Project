import pandas as pd
from pathlib import Path

DATA_IN = Path("C:/Users/computer world/Desktop/Projects/Customer Churn/data/telco_churn.csv")
DATA_OUT = Path("C:/Users/computer world/Desktop/Projects/Customer Churn/data/telco_churn_clean.csv")

def load_and_clean(path):
    df = pd.read_csv(path)

    # Standardize column names
    df.columns = [c.strip() for c in df.columns]

    # Convert total charges to numeric if needed
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Drop duplicates
    df = df.drop_duplicates()

    # Fill or drop missing values (choose conservative approach)
    df = df.dropna(subset=['customerID'])  # ensure id exists

    # For numeric nulls, fill with median
    num_cols = df.select_dtypes(include='number').columns
    for c in num_cols:
        df[c] = df[c].fillna(df[c].median())

    # Convert binary/text churn to 0/1
    if 'Churn' in df.columns:
        df['churn_flag'] = df['Churn'].map({'Yes':1, 'No':0}).fillna(0).astype(int)
    return df

if __name__ == "__main__":
    df = load_and_clean(DATA_IN)
    df.to_csv(DATA_OUT, index=False)
    print(f"Clean file written to {DATA_OUT}")
