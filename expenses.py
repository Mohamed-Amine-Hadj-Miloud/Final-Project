import pandas as pd
import streamlit as st
try:
    data = pd.read_csv('transactions.csv')
except FileNotFoundError:
    data= pd.DataFrame(columns=['Date', 'Name','Type','Amount'])
st.title("Expense tracker")
with st.sidebar:
    name = st.text_input("Input the name of your transaction:")
    date = st.date_input("Input the date of the transaction")
    Type = st.radio("Select the type of your transaction:",["Expense","Earning"])
    if Type == "Earning":amount = st.number_input("Input how much you gained:")
    elif Type == "Expense":amount = st.number_input("Input how much you spent:")
if st.sidebar.button("Save"):
    expenses = pd.DataFrame([{"Date":date,"Name":name,"Type":Type,"Amount":amount}])
    data = pd.concat([data,expenses],ignore_index=True)
    data.to_csv("transactions.csv",index=False)
st.dataframe(data,width=1000)
st.line_chart(data,y='Date',x="Amount",color="Type")