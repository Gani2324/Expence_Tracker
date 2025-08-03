
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.title("💸 Expense Tracker")

# Load or create
try:
    df = pd.read_csv("expenses.csv")
except:
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])

# Add Expense
with st.form("Add Expense"):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Others"])
    amount = st.number_input("Amount", min_value=0.0)
    submit = st.form_submit_button("Add")

if submit:
    df = df.append({"Date": date, "Category": category, "Amount": amount}, ignore_index=True)
    df.to_csv("expenses.csv", index=False)
    st.success("Added successfully!")

# Show data
st.subheader("Expense History")
st.dataframe(df)

# Chart
if not df.empty:
    st.subheader("Spending by Category")
    chart = df.groupby("Category")["Amount"].sum()
    st.bar_chart(chart)
