# 📊 Expense Tracker Project  

A personal **Expense Management System** built using **Python, FastAPI, Streamlit, and MySQL**.  
This project was done as part of the [Codebasics](https://codebasics.io/) course to learn **end-to-end application development** — from backend API design to frontend analytics.  

## Project Structure

- **Frontend/**: Contains the Streamlit application code.
- **Backend/**: Contains the FastAPI backend server code.
- **Tests/**: Contains the test cases for both frontend and backend
- **requirements.txt**: Lists the required Python packages.

## 🚀 Features  

### 1. Expense Management (CRUD Operations)  
- Add, update, delete, and view expenses.  
- Store expense details like **date, amount, category, and notes** in MySQL.  

### 2. Backend (FastAPI)  
- Developed REST API endpoints for:  
  - Adding expenses  
  - Fetching expenses by date  
  - Generating category-wise summaries  
  - Getting monthly analytics  
- Added **logging** for debugging and tracking API activity.  

### 3. Frontend (Streamlit)  
- User-friendly interface to manage expenses.  
- Interactive dashboard for analytics.  

### 4. Analytics  
- **Category-wise analytics**: Understand spending habits across categories.  
- **Monthly analytics**: Track expenses month by month with simple visualizations.  



## 🛠️ Tech Stack  

- **Python** 🐍  
- **FastAPI** ⚡ – Backend API  
- **Streamlit** 🎨 – Frontend & Visualization  
- **MySQL** 🗄️ – Database  
- **Uvicorn** 🚀 – ASGI Server  



## ⚙️ Setup Instructions  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/sanjanagajula/Expense_Tracking_System.git
   cd Expense_Tracking_System
   ```
2. **Install dependencies:**
   ```commandline
   pip install -r requirements.txt
   ```
3. **Run the FastAPI server:**
   ```commandline
   uvicorn server.server:app --reload
   ```
4. **Run the Streamlit app:**
   ```commandline
   streamlit run frontend/app.py
   ```
