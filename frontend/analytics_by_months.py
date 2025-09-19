import streamlit as st
import requests
import pandas as pd

API_URL = "https://expense-tracking-system-3.onrender.com"

def analytics_by_months_tab():
    response = requests.get(f"{API_URL}/analytics/monthly")

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)

        st.title("Expense Breakdown BY Month")

        st.bar_chart(
            data=df.set_index("month")["total"],
            use_container_width=True
        )

        df["total"] = df["total"].map("{:,.2f}".format)
        st.table(df)
    else:
        st.error("Failed to fetch data")

