import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# uv add matplotlib

st.title("Simple Data Dasboard")



uploaded_file=st.file_uploader("Choose CVS file",type="csv") 

if uploaded_file is not None:
    st.write("File uploaded:")
    df=pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filter Data")
    columns=df.columns.tolist()
    selected_columns=st.selectbox("Select Columns to filter",columns)
    unique_values=df[selected_columns].unique()
    selected_value=st.selectbox("Select Value",unique_values)
    
    filtered_data=df[df[selected_columns]==selected_value]
    st.write(filtered_data)
    
    st.subheader("plot Data")
    x_columns=st.selectbox("Select X-axis",columns)
    y_columns=st.selectbox("Select Y-axis",columns)
    
    if st.button("Generate Plot"):
            st.line_chart(filtered_data[[x_columns,y_columns]])
    else:
        st.write("wait for it")
            
    
    
    
    