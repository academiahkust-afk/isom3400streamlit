import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Business Data Dashboard")

# Introduction text
st.write("This dashboard helps visualize sales data over time.")

# Sample data
date_rng = pd.date_range(start='1/1/2023', end='12/31/2023', freq='M')
df = pd.DataFrame(date_rng, columns=['date'])
df['sales'] = np.random.randint(100, 500, size=(len(date_rng)))

# Data visualization with Streamlit
st.subheader("Monthly Sales Data")
st.line_chart(df.set_index('date'))

# Adding a slider for user input
sales_threshold = st.slider("Sales threshold", 100, 500, 300)

# Filtering and displaying data based on user input
filtered_data = df[df['sales'] >= sales_threshold]
st.write(f"Months with sales above {sales_threshold}")
st.write(filtered_data)


num1=st.number_input("Enter the first number: ") 
num2=st.number_input("Enter the second number: ") 

operation=st.selectbox("Select the operation:",["Add","Subtract","Multiply","Divide"])

if st.button("Calculate"):
  if operation=="Add":
    result=(num1+num2)
  if operation=="Subtract":
    result=(num1-num2)
  if operation=="Multiply":
    result=(num1*num2)
  if operation=="Divide":
    result=(num1/num2) if num2!=0 else st.write("Cannot divide by 0")

st.success(f"Result: {result}")
