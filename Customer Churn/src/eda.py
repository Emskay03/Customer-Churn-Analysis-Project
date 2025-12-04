import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "telco_churn_clean.csv"
OUT = Path(__file__).resolve().parents[1] / "data" / "eda_outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

if 'churn_flag' not in df.columns:
    if 'Churn' in df.columns:
        df['churn_flag'] = (
            df['Churn'].astype(str).str.strip().str.lower()
              .map({'yes': 1, 'no': 0})
              .fillna(0).astype(int)
        )
    else:
        raise ValueError("No churn_flag or Churn column found in dataset.")

churn_rate = df['churn_flag'].mean()
print(f"Overall churn rate: {churn_rate:.2%}")

numeric = df.select_dtypes(include=['int64', 'float64'])
if 'churn_flag' in numeric.columns:
    corr = numeric.corr()['churn_flag'].sort_values(ascending=False)
    corr.to_csv(OUT / 'numeric_corr_with_churn.csv')
    print("Saved correlation table")

for c in ['Contract', 'PaymentMethod', 'InternetService']:
    if c in df.columns:
        pivot = (
            df.groupby(c)['churn_flag']
              .agg(['mean', 'count'])
              .reset_index()
              .rename(columns={'mean': 'churn_rate'})
        )
        pivot.to_csv(OUT / f'churn_by_{c}.csv', index=False)

if 'tenure' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='churn_flag', y='tenure', data=df)
    plt.title('Tenure distribution by churn')
    plt.savefig(OUT / 'tenure_by_churn.png', bbox_inches='tight')
    plt.close()
    print("Saved tenure_by_churn.png")
