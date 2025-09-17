Expense Tracking System

An end-to-end Expense Tracking System built as part of the Codebasics
 project.
This project helps users manage their daily expenses with features like CRUD operations, analytics by category and month, and a clean frontend interface.

The system is built using:

FastAPI (Backend API)

MySQL (Database)

Streamlit (Frontend UI)

Python (Core business logic & logging)

🚀 Features

Add, update, and delete expenses

View expenses by date

Analytics by category and month (visualized in Streamlit)

Logging for better debugging and maintainability

Clean separation of backend and frontend

🛠️ Tech Stack

Backend: FastAPI

Frontend: Streamlit

Database: MySQL

Language: Python

⚙️ Setup Instructions

Follow these steps to set up and run the project locally:

1️⃣ Clone the Repository
git clone https://github.com/sanjanagajula/Expense_Tracking_System.git
cd Expense_Tracking_System

2️⃣ Create & Activate Virtual Environment
python -m venv venv


Activate it:

On Windows:

.\venv\Scripts\activate


On Mac/Linux:

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup MySQL Database

Log into MySQL Workbench (or your preferred client) and run:

CREATE DATABASE expense_manager;

USE expense_manager;

CREATE TABLE expenses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  expense_date DATE NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  category VARCHAR(50),
  notes TEXT
);

5️⃣ Configure Database Connection

In db_helper.py, update the connection details as per your MySQL setup:

host="localhost"
user="root"
password="root"
database="expense_manager"

6️⃣ Run FastAPI Backend

From the backend folder, run:

uvicorn server:app --reload


Now open 👉 http://127.0.0.1:8000/docs
 to access API documentation.

7️⃣ Run Streamlit Frontend

From the frontend folder, run:

streamlit run app.py


This will launch the Expense Tracker UI in your browser.

📊 Project Highlights

Implemented CRUD operations for expense management

Built REST API endpoints for backend logic

Added logging for debugging and reliability

Developed an interactive Streamlit frontend

Created analytics dashboards (by category & by month)
