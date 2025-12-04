import pandas as pd
from pandasql import sqldf
from pathlib import Path

pysqldf = lambda q: sqldf(q, globals())
df = pd.read_csv("C:/Users/computer world/Desktop/Projects/Customer Churn/data/telco_churn_clean.csv")

# SQL queries
q1 = """
SELECT PaymentMethod, 
       COUNT(*) as total_customers,
       SUM(churn_flag) as churners,
       ROUND(100.0*SUM(churn_flag)/COUNT(*),2) as churn_pct
FROM df
GROUP BY PaymentMethod
ORDER BY churn_pct DESC
"""
payment_churn = pysqldf(q1)
payment_churn.to_csv('C:/Users/computer world/Desktop/Projects/Customer Churn/data/payment_churn_summary.csv', index=False)

q2 = """
SELECT Contract,
       COUNT(*) as total_customers,
       SUM(churn_flag) as churners,
       ROUND(100.0*SUM(churn_flag)/COUNT(*),2) as churn_pct
FROM df
GROUP BY Contract
ORDER BY churn_pct DESC
"""
contract_churn = pysqldf(q2)
contract_churn.to_csv('C:/Users/computer world/Desktop/Projects/Customer Churn/data/contract_churn_summary.csv', index=False)

print("Exported SQL-style summary tables for Tableau")
