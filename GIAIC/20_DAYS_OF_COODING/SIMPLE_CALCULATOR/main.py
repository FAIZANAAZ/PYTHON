import streamlit as st 

def main():
    st.title("Simple Calculator")
    st.write("Enter the two numbers")
    
    col1,col2=st.columns(2)
        
    with col1:  num1=st.number_input("Enter the first number",value=0.0)
    
    with col2:  num2=st.number_input("Enter the second number",value=0.0)
    
    operation=st.selectbox("Select the operation",("Addition(+)","Subtraction(-)"," Multiplication(*)","Division(/)"))
    
    if st.button("Calculate"):
      try:   
        if operation=="Addition(+)":
            result=num1+num2
            symbol="+"
        elif operation=="Subtraction(-)":
            result=num1-num2
            symbol="-"
        elif operation=="Multiplication(*)":
            result=num1*num2
            symbol="*"
        else:
            if num2==0:
                st.error("Division by zero is not allowed")
                return
            
            result=num1/num2
            symbol="/"
        st.success(f"The result of {num1} {symbol} {num2} is {result}")
            
      except Exception as e:
          st.error(f"Error in occurred : {e}")   
          
if __name__=="__main__":
    main()       