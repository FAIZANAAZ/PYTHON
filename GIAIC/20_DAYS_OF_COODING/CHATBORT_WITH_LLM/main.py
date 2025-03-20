# uv add google-generativeai python-dotenv chainlit

import google.generativeai as gi
from dotenv import load_dotenv
import chainlit as cl
import os 

load_dotenv()
# ye env ki file khod hi load krlyga 
gi.configure(api_key = os.environ.get("GEMINI_API_KEY"))

model = gi.GenerativeModel(
    model_name = "gemini-2.0-flash",
)

# response = model.generate_content("how is llm working?")

# print(response.text)
# ye terminal ke liye tha 

# ui 
@cl.on_chat_start
# isy pora ui bna a jayga 
async def start():
    await cl.Message(content="Hello! How can I help you today?").send()
    # ye ak heading ki trha auto nazr ayga sbsy phlyy 
    
@cl.on_message
# ye user sy message leny ka kam kryga 
async def handle_message(message:cl.Message):
        prompt=message.content
        # ye content user ka input he
        
        response = model.generate_content(prompt)
        response_text=response.text if hasattr(response, "text") else None
    
        await cl.Message(content=response_text).send()
        # ye response model sy bhejyga
      