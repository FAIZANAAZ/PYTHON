import streamlit as st

st.title("Login System")

username = st.text_input("Enter username:")
password = st.text_input("Enter password:", type="password")

if st.button("Login"):
    if username == "admin" and password == "123":
        st.session_state["logged_in"] = True
        st.switch_page("pages/about.py")  # Redirect to About page
    else:
        st.error("Invalid credentials!")
