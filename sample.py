import streamlit as st
st.title("BOOKING TICKETS")
st.header("HELLO ARMY")
st.subheader("Basic Details:")
name1 = st.text_input("Enter Your Name:",key = "name1")
age1= st.number_input("Enter Your Age:",key = "age1")
if st.button("Submit", key="btn1"):
   st.write("Name:", name1)
   st.write("Age:",age1)
st.divider()

st.subheader("Ticket Details:")
ticket = st.number_input("Enter no of tickets:")
if st.button("Next")
st.divider()



