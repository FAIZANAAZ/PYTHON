import time
import streamlit as st

with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(label="Download complete!", state="complete", expanded=False)

st.button('Rerun')

# ismy ye hota ke phliwirt run hogi baqi thori blur honginichy ki phit jb oskatimecomplte hoga 2 seocondka wo highlit
# ho jaygi 