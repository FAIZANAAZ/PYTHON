# https://docs.streamlit.io/library/api-reference/layout/st.empty

# Inserts a container into your app that can be used to hold a single element. 

import streamlit as st
import time

st.title("Pakistan")


with st.empty():
    # empty function ka kam ye he ke loop jo he wo one by one chalta he jesy 
    # 10
    # 9
    # 8
    # 7
    # is trha  line sy lekin emty sy ye hoga ke code ak hi jga  pr rh kr overrite ho jayga jesy 10 phir 10 htyga 9 
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
        # 101 second kedarmiyan sy print hoga one  by one 
    st.write("✔️ 10 seconds over!")

st.write("Pakistan zinda bad")
