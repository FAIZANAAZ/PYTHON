import streamlit as st

def bmi(height, weight):
    if height <= 0 or weight <= 0:  # Negative ya zero values handle karna zaroori hai
        return None
    return weight / ((height / 100) ** 2)

st.title("BMI CALCULATOR")

user_hight = st.number_input("Enter your height in cm", min_value=1.0)
user_weight = st.number_input("Enter your weight in kg", min_value=1.0)

bmi_value = bmi(user_hight, user_weight)

if bmi_value:
    st.success(f"Your BMI is {bmi_value:.2f}")  # f-string ka use kia gya hai
else:
    st.error("Please enter valid height and weight.")

st.write("### BMI Categories ###")
st.write("- **Underweight**: BMI less than 18.5")
st.write("- **Normal weight**: BMI between 18.5 and 24.9")
st.write("- **Overweight**: BMI between 25 and 29.9")
st.write("- **Obesity**: BMI 30 or greater")
