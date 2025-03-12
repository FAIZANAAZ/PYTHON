import streamlit as st  # Streamlit library ko import kar rahe hain jo ek simple web app banane ke liye use hoti hai
import random  # Random module ko import kar rahe hain jo random cheezain generate karne ke liye use hota hai
import time  # Time module ko import kar rahe hain jo delay ya timing operations ke liye use hota hai

st.title("QUIZ APPLICATION")  # Web page ka title set kar rahe hain

# Ek list banai jo multiple questions store karti hai, har question ek dictionary me hai
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad"
    },
    {
        "question": "Which is the largest continent by area?",
        "options": ["Africa", "Asia", "Europe", "Australia"],
        "answer": "Asia"
    },
    {
        "question": "Who wrote the national anthem of Pakistan?",
        "options": ["Allama Iqbal", "Hafeez Jalandhari", "Faiz Ahmed Faiz", "Ahmed Faraz"],
        "answer": "Hafeez Jalandhari"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yuan", "Yen", "Won", "Ringgit"],
        "answer": "Yen"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "answer": "Nile"
    },
    {
        "question": "Which country is famous for the Eiffel Tower?",
        "options": ["Germany", "France", "Italy", "Spain"],
        "answer": "France"
    },
    {
        "question": "Who discovered gravity?",
        "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
        "answer": "Isaac Newton"
    },
    {
        "question": "What is the national language of Pakistan?",
        "options": ["Punjabi", "Sindhi", "Urdu", "Pashto"],
        "answer": "Urdu"
    },
    {
        "question": "Which ocean is the largest by surface area?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "answer": "Pacific Ocean"
    }
]

# Agar "current_question" session state me nahi hai to ek random question set kar do
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Current question ko session state se le kar variable me store kar rahe hain

# 1️⃣ Agar current_question session me pehle se hai → wahi question rahega
# 2️⃣ Agar nahi hai → Random question select hoga
# 3️⃣ question variable me wahi store hoga jo session state me hai



question = st.session_state.current_question       

# Question ko screen par dikhane ke liye subheader use kar rahe hain
st.subheader(question["question"])

# User se answer lene ke liye ek dropdown box (select box) create kar rahe hain
selected_option = st.radio("CHOOSE YOUR ANSWER", question["options"], key="answer")

# Jab user "SUBMIT" button dabaye to jawab check karna hai
if st.button("SUBMIT"):
    if selected_option == question["answer"]:  
        st.success("CORRECT ANSWER")  # Agar jawab sahi hai to success message show karo
    else:
        st.error(f"INCORRECT ANSWER, CORRECT ANSWER IS {question['answer']}")  # Agar jawab galat hai to error message dikhao

    time.sleep(2)  # 2 second ka delay taake user jawab dekh sake

    # Naya random question select kar ke session state me store kar rahe hain
    st.session_state.current_question = random.choice(questions)
    
    # Page ko refresh kar rahe hain taake naya sawal aaye
    st.rerun()
