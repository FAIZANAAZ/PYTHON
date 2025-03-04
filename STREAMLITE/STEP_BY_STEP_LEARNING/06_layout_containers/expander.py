# https://docs.streamlit.io/library/api-reference/layout/st.expander

import streamlit as st

# st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're guaranteed to be random.")
    st.image("https://static.streamlit.io/examples/dice.jpg")
 # ye function bhut acha he ye ak slid ki trha animation me open hoga or sirf  See explanation parameter me
#  jolikhengy wo dikhayga or osprclick krengy to apny anderki baqi chizen dikhayga 