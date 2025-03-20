# first configure in chainlit.yaml

import os 
import chainlit as cl
import google.generativeai as genai
from typing import Optional as Optional, Dict
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

model=genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    
)

@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    row_user_data: Dict[str, str],
    default_user:cl.User,
    # ismy user ki chizen hon name wagera
    
    
)->Optional[cl.User]:
    """
    handle the oauth callback from githup
    return the user object if the user is authenticated
    """
    # print(provider_id,token,row_user_data)
    # only for chacking 
    return default_user

@cl.on_chat_start
async def start():
    
    cl.user_session.set("history",[])
    
    await cl.Message(content="Hello! How can I help you?").send()
@cl.on_message
async def message_handler(message: cl.Message):
    history=cl.user_session.get("history")    
    history.append({"role":"user","content":message.content})
    
    formated_history=[]
    for msg in history:
        role="user" if msg["role"]=="user" else "model"
        formated_history.append({"role":role,"parts":[{"text":msg["content"]}]})
        
    response=await model.generate(formated_history)
    response_text=response.text if hasattr(response,"text") else ""
    
    history.append({"role":"assistant","content":response_text})
    
    cl.user_session.set("history",history)
    
    await cl.Message(content=response_text).send()
        