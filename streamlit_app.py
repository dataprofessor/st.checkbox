import streamlit as st

st.header('st.checkbox')

agree = st.checkbox('I agree')

if agree:
     st.write('Great!')
