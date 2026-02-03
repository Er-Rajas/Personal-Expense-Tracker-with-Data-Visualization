import matplotlib.pyplot as plt
import pandas as pd


def monthly_trend(df):
    s = (
        df[df["amount"] < 0]
        .groupby("month")["amount"]
        .sum()
        .abs()
        .reset_index()
    )

    plt.figure(figsize=(8, 4))
    plt.plot(s["month"], s["amount"])
    plt.xticks(rotation=45)
    plt.title("Monthly Spend")
    plt.tight_layout()
    plt.show()


def category_donut(df, month):
    s = (
        df[(df["amount"] < 0) & (df["month"] == month)]
        .groupby("category")["amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(5, 5))
    plt.pie(
        s.values,
        labels=s.index,
        wedgeprops={"width": 0.5}
    )
    plt.title(f"Category Split — {month}")
    plt.tight_layout()
    plt.show()

