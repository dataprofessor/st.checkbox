import streamlit as st

st.header('st.checkbox')

st.write ('Do you want ice cream?')

yes = st.checkbox('Yes')
no = st.checkbox('No')

if yes:
     st.write("Great! Here's some more 🍦")
     
if no: 
     st.write("Okay, here's some coffee ☕")
