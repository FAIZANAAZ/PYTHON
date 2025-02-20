import streamlit as st

st.title("game select number") #isy title ka name ayga
st.write("Hi faiza")# YE text display karega
st.sidebar.header("Sidebar")#sidebar ka name ayga

number=st.slider("pick a number",100,50,2) #phla number start dosra number end third number step yani jo number dengy slide open hokr ospr roka hoga
st.write(number *2)# yha hmny user ka data save krky dikha bhi diya or double bhi kryga number ko

st.header("this is a header") # ye h1
st.subheader("this is a subheader") # ye h2
st.markdown(" # this is a markdown")# ye markdown esa hota he ke jitny hash lgaygy otny size chota hota jayga 
st.markdown(" ## this is a markdown")
st.markdown(" ### this is a markdown")
st.text("this is a text")# ye p

st.code("""
        st.header("this is a header") # ye h1
st.subheader("this is a subheader") # ye h2
st.markdown(" # this is a markdown")# ye markdown esa hota he ke jitny hash lgaygy otny size chota hota jayga 
st.markdown(" ## this is a markdown")
st.markdown(" ### this is a markdown")
st.text("this is a text")# ye p

        """)# ye code disply kryga documents ki trha 

st.chat_input("this is a chat input")
st.date_input("this is a date input")
st.time_input("this is a time input")# ye date time input kryga

st.selectbox("select a number",["1","2","3","4","5"])#ye select box kryga yani dropdown menu

# ye wo select box hai jo selectbox ka use krta hai
st.radio("select a number",["1","2","3","4","5"])#ye radio button kryga

# ye checkbox ka use krta hai
st.checkbox("select a number",["1","2","3","4","5"])#ye checkbox kryga
st.balloons()
