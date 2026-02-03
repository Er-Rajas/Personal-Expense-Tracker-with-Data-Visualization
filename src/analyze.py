import sqlite3
import pandas as pd


def fetch_frame(db_path="db/expenses.db"):
    con = sqlite3.connect(db_path)

    query = """
        SELECT
            t.tx_date,
            t.description,
            t.amount,
            t.account,
            c.name AS category
        FROM transactions t
        LEFT JOIN categories c ON c.id = t.category_id
    """

    df = pd.read_sql_query(query, con, parse_dates=["tx_date"])
    con.close()

    df["month"] = df["tx_date"].dt.to_period("M").astype(str)
    return df


def kpis(df):
    out = {}

    out["total_spend"] = -df.loc[df["amount"] < 0, "amount"].sum()
    out["income"] = df.loc[df["amount"] > 0, "amount"].sum()
    out["savings"] = out["income"] - out["total_spend"]

    out["top_categories"] = (
        -df[df["amount"] < 0]
        .groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    return out
