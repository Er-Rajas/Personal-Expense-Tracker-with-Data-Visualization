import streamlit as st

from analyze import fetch_frame, kpis
from budget import check_budget
from ingest import read_bank_csv, upsert_transactions


st.set_page_config(
    page_title="Personal Expense Tracker",
    layout="wide"
)

st.title("💸 Personal Expense Tracker")

# -----------------------------
# Upload & Ingest CSV
# -----------------------------
uploaded_file = st.file_uploader("Upload CSV file")

if uploaded_file:
    df_upload = read_bank_csv(
        uploaded_file,
        account="Manual",
        date_col="Date",
        desc_col="Narration",
        amt_col="Amount"
    )
    upsert_transactions(df_upload)
    st.success(f"Ingested {len(df_upload)} transactions")


# -----------------------------
# Load Data
# -----------------------------
df = fetch_frame()

months = sorted(df["month"].unique())
selected_month = st.selectbox("Select Month", months[::-1])

accounts = sorted(df["account"].unique())
selected_accounts = st.multiselect(
    "Select Accounts",
    accounts,
    default=accounts
)

filtered_df = df[
    (df["month"] == selected_month) &
    (df["account"].isin(selected_accounts))
]

# -----------------------------
# KPIs
# -----------------------------
metrics = kpis(filtered_df)

c1, c2, c3 = st.columns(3)
c1.metric("Total Spend", f"₹{metrics['total_spend']:.0f}")
c2.metric("Income", f"₹{metrics['income']:.0f}")
c3.metric("Savings", f"₹{metrics['savings']:.0f}")

# -----------------------------
# Charts
# -----------------------------
st.subheader("Category-wise Spend")
st.bar_chart(
    -filtered_df[filtered_df["amount"] < 0]
    .groupby("category")["amount"]
    .sum()
)

st.subheader("Monthly Trend")
st.line_chart(
    -df[df["amount"] < 0]
    .groupby("month")["amount"]
    .sum()
)

# -----------------------------
# Budget Check
# -----------------------------
st.subheader("Budget Status")
st.dataframe(check_budget(selected_month))
