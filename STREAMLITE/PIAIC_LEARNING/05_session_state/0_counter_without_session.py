''' 
Counter with Session State
No matter how many times we press the Increment button in 
the above app, the count remains at 1. Let's understand why:

Each time we press the Increment button, Streamlit reruns 
counter_without_session.py from top to bottom, and with every run, count 
gets initialized to 0 .

Pressing Increment subsequently adds 1 to 0, thus count=1
no matter how many times we press Increment.

'''

import streamlit as st

st.title('Counter Example')
count = 0

increment = st.button('Increment')
if increment:
    count += 1
    # ismy wo  0 sy 1 hoga phir 0 sy 1 agy nhi bryga kioky streamlit hr bar rerun hota he to wo wapas 0 initilize ho jayga
    

st.write('Count = ', count)