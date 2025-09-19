import mysql.connector
from contextlib import contextmanager
from backend.logging_setup import setup_logger
import os


@contextmanager
def get_db_cursor(commit=False):
    conn = mysql.connector.connect(
        host=os.environ["dpg-d36jdljipnbc7398fn1g-a"],
        user=os.environ["expenses_gvt2_user"],
        password=os.environ["LREPTobNgK56Rgagub1nluYXGACysOtI"],
        database=os.environ["expenses_gvt2"],
        port=int(os.environ["5432"])
    )
    try:
        cursor = conn.cursor(dictionary=True)
        yield cursor
        if commit:
            conn.commit()
    finally:
        cursor.close()
        conn.close()


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start: {start_date}, end: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
    '''SELECT category, SUM(amount) as total 
                FROM expenses WHERE expense_date 
                BETWEEN %s and %s
                GROUP BY category''',
            (start_date, end_date)
        )
        data = cursor.fetchall()
        return data

    ###
def fetch_all_monthly_expenses():
    with get_db_cursor() as cursor:
        cursor.execute(
            """
            SELECT 
                DATE_FORMAT(expense_date, '%M %Y') AS month, 
                SUM(amount) AS total
            FROM expenses
            GROUP BY DATE_FORMAT(expense_date, '%M %Y')
            ORDER BY MIN(expense_date);
            """
        )
        return cursor.fetchall()

##


if __name__ == '__main__':

    expenses = fetch_expenses_for_date("2024-08-01")
    print(expenses)
    summary= fetch_expense_summary("2024-08-01", "2024-08-05")
    for record in summary:
        print(record)



