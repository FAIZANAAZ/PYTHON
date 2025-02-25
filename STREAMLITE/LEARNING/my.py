import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #pip install matplotlib


st.title("Yeh ek Title hai")  # Bara Title
st.header("Yeh ek Header hai")  # Section ka header
st.subheader("Yeh ek Subheader hai")  # Chhota header
st.write("Normal text likhne ke liye `st.write()` use hota hai.")
st.markdown("**Yeh bold text hai** aur *yeh italic text hai*")  # Markdown support

if st.button("Click karo!"):
    st.write("Button click ho gaya!")
    
    
    # //////////////////////////////////////////////////////////////////////////////////////////
    
agree = st.checkbox("Mujhe yeh pasand aya")
if agree:
    st.write("Shukriya!")
    
    # ye checkbox tik lgany wala
    
    # //////////////////////////////////////////////////////////////////////////////////////////
    
option = st.selectbox("Konsa fruit pasand hai?", ["Apple", "Mango", "Banana"])
st.write("Tumne select kiya:", option)
if option == "Apple":
    st.write(f"Apple khao")
else:
    st.write(f"{option} khao")



#//////////////////////////////////////////////////////////////////////////////////////////

uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # pd ko pandas sy import krna hoga 
    st.write(df)
    
# ////////////////////////////////////////////////////////////////////////////////////////// 
    
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)  # Line chart
st.bar_chart(chart_data)  # Bar chart

fig, ax = plt.subplots()
ax.hist(np.random.randn(100), bins=20)
st.pyplot(fig) 

# ye mokhtafi chart hai jo hmny display kraya hai

 #////////////////////////////////////////////////////////////////////////////////////////
 
#  ye ak page sy dosra page pr jany wala code hai

# Sidebar me navigation options
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])
# radio yani jesy mcq me hota he click krny wala gol button

# Home Page
# if page == "Home":
#     st.empty()
#     from home import home
#     home_page = st.Page(home, title="Home", icon="🏠")
#     # ye page homelera he or title or iconye tab keliye set ory hen g
#     pg = st.navigation([home_page])

#     # Current page ko run karein
#     pg.run()
    
# ////////////////LOGIN SYSTEM //////////////////////////
    
st.title("Login System")

username = st.text_input("Enter username:")
password = st.text_input("Enter password:", type="password")

if st.button("Login"):
    if username == "admin" and password == "123":
        st.session_state["logged_in"] = True
        st.switch_page("about.py")  # Redirect to About page
    else:
        st.error("Invalid credentials!")
