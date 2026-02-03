# Personal Expense Tracker with Data Visualization

## 📌 Project Overview

The **Personal Expense Tracker with Data Visualization** is a Python-based application designed to help users record, categorize, analyze, and visualize their personal income and expenses.
It provides clear financial insights through automated categorization, budget tracking, interactive dashboards, and downloadable reports.

This project demonstrates core data engineering and data analysis concepts such as data ingestion, cleaning, database design, aggregation, visualization, and reporting.

---

## 🎯 Objectives

* Track income and expenses from CSV files
* Automatically categorize transactions using rule-based logic
* Store data persistently using SQLite
* Analyze spending patterns and savings
* Visualize expenses using charts
* Set monthly budgets and detect overspending
* Export monthly reports to Excel
* Provide an interactive dashboard using Streamlit

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Database:** SQLite
* **Libraries:**

  * pandas
  * matplotlib
  * streamlit
  * xlsxwriter
  * pytest
* **Visualization:** Matplotlib, Streamlit charts
* **Reporting:** Excel (.xlsx)

---

## 📂 Project Structure

```
Personal-Expense-Tracker-with-Data-Visualization/
│
├── data/                 # Input CSV files
├── db/                   # SQLite database
├── exports/              # Generated Excel reports
├── src/
│   ├── analyze.py        # KPI & aggregation logic
│   ├── app_streamlit.py  # Streamlit dashboard
│   ├── budget.py         # Budgeting logic
│   ├── categorize.py     # Rule-based categorization
│   ├── ingest.py         # CSV ingestion & cleaning
│   ├── models.py         # Database schema
│   ├── plots.py          # Visualization utilities
│   └── report.py         # Excel report generation
│
├── tests/                # Unit tests
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## ⚙️ Features

### 1. Data Ingestion

* Upload bank or manual CSV files
* Normalize date, description, and amount fields
* Prevent duplicate transactions

### 2. Automatic Categorization

* Rule-based keyword matching (Food, Transport, Shopping, etc.)
* Income detection based on positive amounts
* Fallback to `Uncategorized`

### 3. Analysis & KPIs

* Monthly spending totals
* Category-wise expense breakdown
* Income, expenses, and savings calculation

### 4. Budgeting

* Set monthly category budgets
* Compare actual spending vs budget
* Identify overspending

### 5. Visualization

* Monthly expense trend (line chart)
* Category-wise expense distribution (donut & bar charts)

### 6. Dashboard (Streamlit)

* Upload CSV files
* Filter by month and account
* View KPIs and charts interactively
* Display budget status

### 7. Reporting

* Export monthly transactions to Excel
* Category-wise summary in a separate sheet

### 8. Testing

* Unit tests for ingestion and categorization logic using pytest

---

## ▶️ How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Initialize Database

```bash
python -c "from src.models import init_db; init_db()"
```

### 3. Run the Dashboard

```bash
streamlit run src/app_streamlit.py
```

### 4. Run Tests

```bash
pytest
```

---

## 📊 Sample Output

* Interactive dashboard showing:

  * Total Spend
  * Income
  * Savings
* Monthly trend line
* Category-wise expense breakdown
* Budget comparison table
* Excel report with:

  * Transactions sheet
  * Category summary sheet

---

## 🔍 Key Learnings

* Designing normalized database schemas
* Handling real-world CSV inconsistencies
* Rule-based text categorization
* Separating data logic from UI logic
* Building end-to-end data applications in Python
* Creating reproducible and testable codebases

---

## 🚀 Possible Extensions

* OCR-based receipt scanning
* Email alerts for budget overshoot
* Recurring expense automation
* Machine learning-based categorization
* Multi-currency support with exchange rates

---

## 👤 Author

**Rajas**
Python & Data Science Enthusiast | Engineer Student

---

## 📄 License

This project is licensed under the CC0 1.0 Universal.
