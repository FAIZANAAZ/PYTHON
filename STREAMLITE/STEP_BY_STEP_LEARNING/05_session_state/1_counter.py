import streamlit as st

st.title('Counter Example')

# st.write(st.session_state)

if 'count' not in st.session_state:
    st.session_state.count = 0
#  count ak variable he jb hm kisi variable ko season e sath chahlty hen to wo osky ander
# store ho jata he hm dekhgy ke agr wo season me nhi he yani phly bar chl rha he to wo 0 ho jayga    

increment = st.button('Increment')
if increment:
    st.session_state.count += 1
# Jab bhi aap Streamlit app mein kisi variable ko store karna chahein jo app ke rerun hone par reset na ho, tab st.session_state ka use kiya jata hai.
    #yani again 0 ho jayga agr reset howa     

st.write('Count = ', st.session_state.count)
# del st.session_state.count
"Text" , st.session_state.count