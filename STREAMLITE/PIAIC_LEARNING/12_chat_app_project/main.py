import streamlit as st
import random

# اس بات کو یقینی بنائیں کہ session_state میں 'messages' لسٹ موجود ہو
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# پہلے سے موجود چیٹ میسجز کو دکھائیں
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# یوزر کے ان پٹ کا انتظار کریں
input_text = st.chat_input("Type a message...")

if input_text:
    # یوزر کا میسج سٹور کریں اور دکھائیں
    st.session_state["messages"].append({"role": "user", "content": input_text})
    with st.chat_message("user"):
        st.write(input_text)

    # اسسٹنٹ کا جواب چنیں
    bot_reply = random.choice([
        "Hello there! How can I assist you today?",
        "Hi, human! Is there anything I can help you with?",
        "Do you need help?",
    ])
    
    # اسسٹنٹ کا میسج سٹور کریں اور دکھائیں
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
