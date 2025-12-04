# 📊 Customer Churn Analysis Project  

A complete end-to-end data analysis project using **Python (pandas, numpy)** and **Tableau** to understand customer churn drivers in a telecommunications dataset.

---

## 🧠 Project Objective  

The primary goal of this project is to answer:

### **“Which customers are most likely to churn, and why?”**

Customer churn directly impacts revenue and long-term business growth.  
This project identifies key behavioral patterns, risk segments, and actionable insights using structured data analysis and visualization.

---

## 🗂 Dataset  

- **Source:** Telco Customer Churn dataset (cleaned version)  
- **Rows:** 7,043 customers  
- **Target Variable:** `Churn` (Yes/No)  
- **Converted Variable:** `churn_flag` (1 = Churned, 0 = Not Churned)  
- **Features Include:**  
  - Customer demographics  
  - Tenure  
  - Contract type  
  - Payment method  
  - Monthly & total charges  
  - Internet services and add-ons  

---

## 🛠 Tools & Technologies  

| Area | Tools |
|------|-------|
| Programming | Python, Pandas, NumPy |
| Visualization | Tableau |
| Environment | VS Code |
| File Formats | CSV, Tableau Workbook |

---

## 🧹 Data Cleaning & Preparation  

Performed in Python:

- Removed missing values in `TotalCharges`
- Converted `Churn` → `churn_flag` (binary)
- Ensured numerical types for charges & tenure
- Checked distributions & outliers
- Exported cleaned dataset for Tableau usage

Scripts included:
- `eda.py`
- `modeling.py`
- `preprocessing.py` *(if applicable)*

---

## 📈 Dashboard Overview (Tableau)

The Tableau dashboard includes:

### **1. KPI Overview**
- Total customers  
- Churn rate  
- Average monthly charges  
- Average tenure  

### **2. Churn by Contract Type**
- Month-to-month contracts show the highest churn (~42%)

### **3. Churn by Payment Method**
- Electronic check users churn the most (~45%)

### **4. Tenure Distribution (Boxplot)**
- Churned users have significantly lower tenure  
- Most churn happens early in the customer lifecycle  

### **5. Insights Summary**
> Customers on month-to-month contracts and electronic check payments exhibit the highest churn, and churned customers generally have much shorter tenure and slightly higher monthly charges — indicating that early-stage customers with higher billing pressure and lower commitment are the most at-risk segment.

---

## 🔍 Key Insights

- **Low-commitment customers churn more:**  
  Month-to-month contract users are the most vulnerable group.

- **Payment method is a strong indicator:**  
  Electronic check customers churn drastically more than automatic bank/credit transfers.

- **Short tenure strongly predicts churn:**  
  Many customers leave early in their lifecycle.

- **Higher monthly charges correlate with churn:**  
  Cost-sensitive users are more likely to leave.

---

## 🚀 Skills Demonstrated

- Data cleaning & preparation in Python  
- Exploratory data analysis  
- Feature engineering  
- Segmentation & pattern recognition  
- Data visualization in Tableau  
- Dashboard design & storytelling  
- Business insight generation  

---

## 📽 Video Walkthrough

A 3-minute project explanation covering:
- The problem addressed  
- Approach & workflow  
- Dashboard insights  
- Key business recommendations  

*(Optional: Add link once uploaded)*

---

## 📁 Project Structure

