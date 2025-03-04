import streamlit as st

def convert_unit(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000
    }
    
    key = f"{unit_from}_{unit_to}"  # Generate key based on input
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not found"

st.title("Unit Converter")

value = st.number_input("Enter a value", min_value=1.0, step=1.0)
unit_from = st.selectbox("Convert From", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert To", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.success(result)
