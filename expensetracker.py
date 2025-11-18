import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

st.title("Personal Expense Tracker") 
#session state --> retain your old data and be able to add new

if 'expenses' not in st.session_state: 
  st.session_state.expenses=pd.DataFrame(columns=['Date','Category','Amount','Description'])

with st.form("expenses_form"):
  st.subheader("Add New Expense") 
  date = st.date_input("Date") 
  category = st.selectbox("Category",["Food","Transport","Entertainment","Bills","Other"])
  amount = st.number_input("Amount",min_value=0,step = 1)
  description=st.text_input("Description")

submitted=st.form_submit_button("Add Expense")
if submitted:
  new_expense = pd.DataFrame({
  'Date':[date],
  'Category':[category],
  'Amount':[amount],
  'Description':[description]})

  st.session_state.expenses = pd.concat([st.session_state.expenses,new_expense])
  st.success("Expense added!")

if not st.session_state.expenses.empty:
  st.subheader("Your Expenses")
  st.dataframe(st.session_state.expenses)

  st.subheader("Summary") 
  total_spent=st.session_state.expenses['Amount'].sum()
  st.write(f"Total Spent:${total_spent:.2f}")

  category_totals=st.session_state.expenses.groupby('Category')['Amount'].sum()
  
  fig,ax=plt.subplots(figsize=(10,6))
  ax.pie(category_totals.values,labels=category_totals.index)
  ax.set_title("Expenses by Category")
  st.pyplot(fig)
else:
  st.info("No expenses added yet. Add an expense above to get started!")
