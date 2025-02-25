import streamlit as st

st.title("🏠 Home Page")

# Session state me user ka naam save karna
user_name = st.text_input("Enter your name:", key="name")

if st.button("Save Name"):
    st.session_state["user_name"] = user_name
    st.success("Name saved!")
