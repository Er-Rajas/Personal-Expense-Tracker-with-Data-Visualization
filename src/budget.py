import sqlite3
import pandas as pd


def set_budget(month, category, limit, db_path="db/expenses.db"):
    con = sqlite3.connect(db_path)

    con.execute(
        "INSERT INTO budgets(month, category_name, limit_amount) VALUES (?, ?, ?)",
        (month, category, float(limit))
    )

    con.commit()
    con.close()


def check_budget(month, db_path="db/expenses.db"):
    con = sqlite3.connect(db_path)

    spend = pd.read_sql_query(
        """
        SELECT
            c.name AS category,
            -SUM(t.amount) AS spend
        FROM transactions t
        LEFT JOIN categories c ON c.id = t.category_id
        WHERE t.amount < 0
          AND strftime('%Y-%m', t.tx_date) = ?
        GROUP BY c.name
        """,
        con,
        params=[month]
    )

    budgets = pd.read_sql_query(
        "SELECT category_name, limit_amount FROM budgets WHERE month = ?",
        con,
        params=[month]
    )

    con.close()

    merged = budgets.merge(
        spend,
        left_on="category_name",
        right_on="category",
        how="left"
    ).fillna({"spend": 0})

    merged["over_by"] = merged["spend"] - merged["limit_amount"]

    return merged.sort_values("over_by", ascending=False)
