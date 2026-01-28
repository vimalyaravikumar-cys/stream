import streamlit as st
st.title("BOOKING TICKETS")
st.header("HELLO ARMY")
st.subheader("Basic Details:")
name1 = st.text_input("Enter Your Name:",key = "name1")
age1= st.number_input("Enter Your Age:",min_value=1,key = "age1")
if st.button("Submit", key="btn1"):
   st.write("Name:", name1)
   st.write("Age:",age1)
st.divider()

st.subheader("Ticket Details:")
ticket = st.number_input("Enter no of tickets:",min_value=1)
if st.button("Next"):
   st.write("NO Of Tickets:")
st.divider()
st.subheader("Payment Details: ")
payment = st.selectbox("Select a payment mode:", ['Bank Transfer', 'Gpay'])
st.write("Your Pay mode is:", payment)
if st.button("Finish"):
   st.write(st.success("Tickets booked "))