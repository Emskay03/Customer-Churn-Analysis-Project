from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
import joblib

# ---------- 1. Load the CLEAN dataset safely ----------
DATA = Path(__file__).resolve().parents[1] / "data" / "telco_churn_clean.csv"
df = pd.read_csv(DATA)

# ---------- 2. Ensure churn_flag exists ----------
if 'churn_flag' not in df.columns:
    churn_col = None
    for col in df.columns:
        if col.strip().lower() == "churn":
            churn_col = col
            break

    if churn_col is None:
        raise ValueError("No 'churn_flag' or 'Churn' column found in dataset.")

    df['churn_flag'] = (
        df[churn_col].astype(str).str.strip().str.lower()
        .map({'yes': 1, 'no': 0})
        .fillna(0)
        .astype(int)
    )

# ---------- 3. Select features ----------
for col in ['tenure', 'MonthlyCharges', 'TotalCharges']:
    if col not in df.columns:
        raise ValueError(f"Required feature column '{col}' not found in data.")

X = df[['tenure', 'MonthlyCharges', 'TotalCharges']].copy()
y = df['churn_flag']

X = X.fillna(0)

# ---------- 4. Train / test split ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# ---------- 5. Scale + train model ----------
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_s, y_train)

# ---------- 6. Evaluation ----------
y_pred = model.predict(X_test_s)
y_proba = model.predict_proba(X_test_s)[:, 1]

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

roc = roc_auc_score(y_test, y_proba)
print(f"ROC AUC: {roc:.3f}")

# ---------- 7. Save model + scaler ----------
MODEL_DIR = Path(__file__).resolve().parents[1] / "model"
MODEL_DIR.mkdir(exist_ok=True)

joblib.dump(model, MODEL_DIR / "logreg_model.joblib")
joblib.dump(scaler, MODEL_DIR / "scaler.joblib")

print(f"\nModel and scaler saved in: {MODEL_DIR}")
