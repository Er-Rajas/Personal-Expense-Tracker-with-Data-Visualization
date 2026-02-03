import pandas as pd
from src.ingest import read_bank_csv

def test_read_bank_csv_columns(tmp_path):
    csv = tmp_path / "demo.csv"
    csv.write_text(
        "Date,Narration,Amount\n"
        "2025-10-01,Test Expense,-100\n"
    )

    df = read_bank_csv(
        csv,
        account="TEST",
        date_col="Date",
        desc_col="Narration",
        amt_col="Amount"
    )

    assert list(df.columns) == ["tx_date","description","amount","account","raw_source"]
    assert len(df) == 1
