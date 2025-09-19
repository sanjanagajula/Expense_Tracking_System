import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from backend.logging_setup import setup_logger
import os

# Initialize logger
logger = setup_logger("db_helper")

@contextmanager
def get_db_cursor(commit=False):
    """
    Context manager to get a PostgreSQL cursor. Automatically commits if commit=True.
    """
    try:
        conn = psycopg2.connect(
            host=os.environ["DB_HOST"],      
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASS"],
            dbname=os.environ["DB_NAME"],   # in psycopg2 use dbname instead of database
            port=int(os.environ["DB_PORT"])
        )

        cursor = conn.cursor(cursor_factory=RealDictCursor)  # ✅ returns rows as dictionaries
        yield cursor

        if commit:
            conn.commit()

    except psycopg2.Error as e:   # ✅ PostgreSQL error handling
        logger.error(f"Database connection/query error: {e}")
        raise

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


# ------------------------
# Your Queries
# ------------------------

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        return cursor.fetchall()


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
            """
            SELECT category, SUM(amount) as total 
            FROM expenses 
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category
            """,
            (start_date, end_date)
        )
        return cursor.fetchall()


def fetch_all_monthly_expenses():
    with get_db_cursor() as cursor:
        cursor.execute(
            """
            SELECT 
                TO_CHAR(expense_date, 'Month YYYY') AS month,  -- ✅ PostgreSQL syntax
                SUM(amount) AS total
            FROM expenses
            GROUP BY TO_CHAR(expense_date, 'Month YYYY')
            ORDER BY MIN(expense_date);
            """
        )
        return cursor.fetchall()


# ------------------------
# Test Run
# ------------------------
if __name__ == '__main__':
    expenses = fetch_expenses_for_date("2024-08-01")
    print(expenses)
    summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    for record in summary:
        print(record)
