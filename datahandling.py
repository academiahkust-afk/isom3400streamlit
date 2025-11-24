import streamlit as st
import pandas as pd
import os

# Get the current working directory
current_directory = os.getcwd()      #good practice to ensure you get the current directory 
# Define the file path
file_path = os.path.join(current_directory, 'winequality-red.csv')

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, delimiter=';') #delimiter is the separator symbol that your csv file uses 
#df is not just for data (rows and columns) but has a host of other functionality associated with dataframe objects 

# Display the DataFrame in an interactive table
st.write("Wine Quality Data")
st.dataframe(df)

data = {'Product':['A','B','C'],
        'Sales':[1200,850,950],
        'Customers':[300,400,350]}

df2=pd.DataFrame(data)
st.dataframe(df2)                        #Interactive table
st.data_editor(df2)                        #Editable table
st.table(df2)                                #Static table // Table and dataframe are different 

st.dataframe(df.style.format({'Sales':'${:,0f}','Customers':'{:,0f}'}))
