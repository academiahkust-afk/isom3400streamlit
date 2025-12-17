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

st.header("Retail Business Dashboard")
st.subheader("Manager Input Section")
st.write("Please enter the monhtly sales target and select the region.")

sales_target=st.number_input("Enter monthly sales target (in USD)")
region=st.selectbox("Select region",["North","South","East","West"])

if st.button("Submit"):
  st.success(f"Sales Target = {sales_target} set for {region} Region.")

st.form(key="Customer_Feedback_Form"):
  st.subheader("Customer Feedback Form")
  st.product_id = st.text_input("Enter Product ID")
  feedback = st.text_area("Enter your feedback")
  sales_range = st.slider("Select Sales Range", min_value=0, max_value=1500, value=(500, 1000))
  submit_button = st.form_submit_button("Submit Feedback")

if submit_button:
  st.write("### Submitted Feedback")
  st.write(f"**Product:** {product_choice}")
  st.write(f"**Sales Range:** {sales_range}")
  st.write(f"**Product ID:** {product_id}")
  st.write(f"**Feedback:** {feedback}")
