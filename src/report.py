import pandas as pd
import sqlite3


def export_month(month, path="exports/report.xlsx", db_path="db/expenses.db"):
    con = sqlite3.connect(db_path)

    tx = pd.read_sql_query(
        """
        SELECT
            t.tx_date,
            t.description,
            t.amount,
            t.account,
            c.name AS category
        FROM transactions t
        LEFT JOIN categories c ON c.id = t.category_id
        WHERE strftime('%Y-%m', t.tx_date) = ?
        ORDER BY t.tx_date
        """,
        con,
        params=[month]
    )

    summary = (
        -tx[tx["amount"] < 0]
        .pivot_table(
            index="category",
            values="amount",
            aggfunc="sum"
        )
        .sort_values("amount", ascending=False)
    )

    with pd.ExcelWriter(path, engine="xlsxwriter") as writer:
        tx.to_excel(writer, sheet_name="Transactions", index=False)
        summary.to_excel(writer, sheet_name="Category Summary")

    con.close()
    return path
