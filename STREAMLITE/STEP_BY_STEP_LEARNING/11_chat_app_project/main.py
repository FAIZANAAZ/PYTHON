import streamlit as st
import pandas as pd
import numpy as np
import random


st.title("AI CHATBOT")

chat_answer = st.chat_input("Enter your message")

def chatbot():
   response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
   return response

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
    
if chat_answer:
    # Store user input
    st.session_state.chat_history.append(("user", chat_answer))
    
    # Generate chatbot response
    bot_response = chatbot()
    st.session_state.chat_history.append(("assistant", bot_response))    
    
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(message)

       
    
# ye chathistry me jo data jama hora he osmy roleara he ak or ak message to woonkonikal rha he or prinnt krwa rha he     
        


       
       