import streamlit as st

st.title("Business Dashboard with Streamlit Layouts")
st.write("## Objective: To demonstrate the usage of columns, tabs, and dynamic containers in a business dashboard.")
# the use of the 2 # keys = markdown --> helps to format the text you'd like to present

col1, col2, col3 = st.columns(3)
with col1:
    st.header("Q1 2024")
    st.write("Revenue: $1.2M")
with col2:
    st.header("Q2 2024")
    st.write("Revenue: $1.5M")
with col3:
    st.header("Q3 2024")
    st.write("Revenue: $1.3M")
