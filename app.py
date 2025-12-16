import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
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

tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights", "Market Trends"])
with tab1:
    st.write("Content for Sales Data")
    sales_data = {
        "Q1 2024": "$1.2M",
        "Q2 2024": "$1.5M",
        "Q3 2024": "$1.3M",
        "Q4 2024": "$1.6M"
    }
    for quarter, revenue in sales_data.items():
        st.write(f"{quarter}: {revenue}")


with tab2:
    st.write("Content for Customer Insights")
    customer_feedback = [
        "Great service!",
        "Very satisfied with the product quality.",
        "Quick delivery and excellent support."
    ]
    for num,feedback in enumerate(customer_feedback):
        st.write(f"{num+1}. {feedback}") #hyphen is a markdown --> creates a bulletpoint
with tab3:
    st.write("Content for Market Trends")
    market_trends = {
        "Eco-friendly products": "Increasing demand",
        "Online shopping": "Continued growth",
        "Subscription services": "Rising popularity"
    }
    for trend, status in market_trends.items():
        st.write(f"{trend}: {status}")

with st.expander("More Information"):
    st.write("Additional details on data collection methods.")
    st.write("Data was collected through surveys and sales reports.")

placeholder = st.empty()

# Simulate loading data and updating the placeholder
for i in range(5):
    placeholder.write(f"Loading data... {i*20}% complete")
    time.sleep(1) #wait 1 second and then increment from 20, 40 to 80% complete

# Once loading is complete, display the final message
placeholder.write("Data loading complete. Displaying business insights.")

business_insights = [
    "Revenue increased by 15% in Q1 2024.",
    "Customer satisfaction improved by 10%.",
    "Market trends show a growing demand for eco-friendly products."
]
for insight in business_insights:
    placeholder.write(insight)
    time.sleep(2)
'''
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
