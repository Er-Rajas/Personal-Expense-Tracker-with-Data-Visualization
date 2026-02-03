from src.categorize import classify

def test_classify_food():
    assert classify("Swiggy order") == "Food & Dining"

def test_classify_income():
    assert classify("Salary Credit") == "Income"
