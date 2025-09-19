from fastapi import FastAPI
from datetime import date
from backend import db_helper
from typing import List
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str


class DateRange(BaseModel):
    start_date:date
    end_date:date


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expense(expense_date: date):
    expenses=db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database")
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expense: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expense:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    return {"message": "Expense updated successfully"}


@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database")

    total=sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage =(row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage,
        }

    return breakdown

@app.get("/analytics/monthly")
def get_monthly_analytics():
    data = db_helper.fetch_all_monthly_expenses()
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database")
    return data


