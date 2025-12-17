import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

st.header("ISOM3400: Business Dashboard")
st.write("Practicing using Streamlit Functions to create an interactive Web App")

with st.sidebar:
  selected=option_menu(
    menu_title="Menu",
    options=["Home","Customer Feedback","Market Insight"],
    icons=["1-circle-fill","2-circle-fill","3-circle-fill"],
    default_index=0,
  )

if selected=="Home":
  tab1,tab2,tab3,tab4=st.tabs(["Q1 2025","Q2 2025","Q3 2025","Q4 2025"])

  with tab1:
    st.subheader("Revenue:")
    st.write("$1.5M")
    st.subheader("Net Income:")
    st.write("$0.9M")

  with tab2:
    st.subheader("Revenue:")
    st.write("$2.5M")
    st.subheader("Net Income:")
    st.write("$1.2M")

  with tab3:
    st.subheader("Revenue:")
    st.write("$2.2M")
    st.subheader("Net Income:")
    st.write("$1.4M")

  with tab4:
    st.subheader("Revenue:")
    st.write("$2.7M")
    st.subheader("Net Income:")
    st.write("$1.7M")

if selected =="Customer Feedback":
  with st.form(key="feedback_form"):
    product=st.text_input("Enter Product ID: ")
    feedback=st.text_area("Enter Feedback: ")
    price=st.slider("Enter the price paid: ",0,10000,500)
    submit_button=st.form_submit_button('Submit Feedback')

  if submit_button:
    st.success("Feedback Submitted")
    st.write(f"Feedback about {product} purchased at ${price}: {feedback}")

if selected=="Market Insight":
  products=["Shoes","T-shirts","Tops","Dresses","Jeans","Pants","Jumpsuits"]
  sales_nums=np.random.rand(7)*10000
  customers=np.random.randint(10000,size=7)

  sales_data=pd.DataFrame({
    "Products":products,
    "Sales":sales_nums,
    "Customers":customers
  })

  st.bar_chart(sales_data,x="Products",y="Sales")
  
