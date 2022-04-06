import streamlit as st

st.header('st.checkbox')

st.write ('Do you like ice cream?')

yes = st.checkbox('Yes')

if yes:
     st.write("Great! Here's some more 🍦")
