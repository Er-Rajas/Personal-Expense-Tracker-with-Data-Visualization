import pandas as pd
import sqlite3
from datetime import datetime

STANDARD_COLS = ['tx_date','description','amount','account','raw_source']

def read_bank_csv(path,account,date_col,desc_col,amt_col,sep=","):
    df = pd.read_csv(path,sep=sep)
    
    df["tx_date"] = pd.to_datetime(df[date_col]).dt.date.astype(str)
    df['description'] = df[desc_col].astype(str).str.strip()
    df['amount'] = pd.to_numeric(df[amt_col], errors='coerce')  
    df['account'] = account
    df['raw_source'] = path
    return df[STANDARD_COLS].dropna(subset=['tx_date','amount'])

def upsert_transactions(df,db_path="db/expenses.db"):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    rows=df.itertuples(index=False)
    cur.executemany('''
        INSERT OR IGNORE INTO transactions (tx_date, description, amount, account, raw_source)
        VALUES (?, ?, ?, ?, ?)
    ''', rows)
    con.commit()
    con.close()
    
if __name__ == "__main__":
    df = read_bank_csv(r"data/hdfc_oct.csv",account="HDFC",date_col='Date',desc_col='Narration',amt_col='Amount')
    upsert_transactions(df)
