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

# 🎨 Customizing the UI
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Unit Converter</h1>", unsafe_allow_html=True)
st.write("#### Convert between different units easily!")

st.divider()  # 🎚️ Adds a visual separator

# 🌟 Using columns for a better layout
col1, col2 = st.columns(2)

with col1:
    value = st.number_input("🔢 Enter a value", min_value=1.0, step=1.0)

with col2:
    unit_from = st.selectbox("🔄 Convert From", ["meter", "kilometer", "gram", "kilogram"])
    unit_to = st.selectbox("🎯 Convert To", ["meter", "kilometer", "gram", "kilogram"])

st.divider()  # 🎚️ Adds another separator

# 🚀 Styled Convert Button
if st.button("🔁 Convert", use_container_width=True):
    result = convert_unit(value, unit_from, unit_to)
    st.success(f"✅ **Converted Value:** {result}")

