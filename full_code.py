import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.header("ISOM3400: Business Dashboard")
st.write("Practicing using Streamlit Functions to create an interactive Web App")

with st.sidebar:
  selected=option_menu(
    menu_title="title",
    options=["Home","Customer Feedback","Market Insight"],
    icons=["1-circle-fill","2-circle-fill","3-circle-fill"],
    default_index=0,
  )
  
