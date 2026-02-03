import re
import sqlite3
import pandas as pd

RULES = {
    "Groceries": [r"big bazaar|reliance fresh|d-mart|grocery|supermart"],
    "Food & Dining": [r"swiggy|zomato|restaurant|cafe|coffee"],
    "Transport": [r"uber|ola|metro|fuel|petrol|diesel|bus"],
    "Bills & Utilities": [r"electric|water|wifi|broadband|mobile recharge|dth"],
    "Shopping": [r"amazon|flipkart|myntra|ajio"],
    "Entertainment": [r"netflix|amazon prime|spotify|cinema|bookmyshow"],
    "Income": [r"salary|payout|refund|reimbursement"]
}

def classify(description: str) -> str:
    desc = description.lower()
    for category, patterns in RULES.items():
        if any(re.search(p, desc) for p in patterns):
            return category
    return "Uncategorized"


def run(db_path="db/expenses.db"):
    con = sqlite3.connect(db_path)

    # fetch uncategorized transactions
    df = pd.read_sql_query(
        "SELECT id, description, amount FROM transactions WHERE category_id IS NULL",
        con
    )

    # fetch existing categories
    cats = pd.read_sql_query("SELECT id, name FROM categories", con)
    name_to_id = dict(zip(cats["name"], cats["id"]))

    # ensure base categories exist
    for name in set(RULES.keys()) | {"Uncategorized"}:
        if name not in name_to_id:
            con.execute(
                "INSERT INTO categories(name) VALUES (?)",
                (name,)
            )
            con.commit()

    # refresh category map
    cats = pd.read_sql_query("SELECT id, name FROM categories", con)
    name_to_id = dict(zip(cats["name"], cats["id"]))

    # assign categories
    for row in df.itertuples(index=False):
        if row.amount > 0:
            category = "Income"
        else:
            category = classify(row.description)

        con.execute(
            "UPDATE transactions SET category_id=? WHERE id=?",
            (name_to_id[category], row.id)
        )

    con.commit()
    con.close()


if __name__ == "__main__":
    run()
