import os
import chainlit as cl
from typing import Optional, Dict
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool

# Load environment variables from .env
load_dotenv()

# Retrieve GEMINI API Key from environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize OpenAI provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Model initialization
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

# Define a tool to get weather info
@function_tool("get weather")
async def get_weather(location: str, unit: str) -> str:
    """
    Get the weather in a given location.
    """
    return f"The weather in {location} is 22 degrees {unit}."

# Define the agent with instructions for the assistant
agent = Agent(
    name="you are a greeting agent",
    instructions="""You are a greeting agent. Your task is to greet the user in a friendly manner. 
    If anyone speaks 'hi', you respond with 'salam'. If anyone asks about the weather, use the get_weather function (tool). 
    If anyone says 'hello', you respond with 'assalamu alaikum'. 

    If someone asks about Faiza, reply as follows:

    Q: Who is Faiza?  
    A: Faiza is a cute girl, 18 years old, an inventor, and a full-stack developer. She loves Chinese food, shopping, and coding.

    Q: How old is Faiza?  
    A: Faiza is 18 years old.

    Q: What does Faiza do?  
    A: Faiza is an inventor and a full-stack developer. She is also focusing on AI right now.

    Q: Where does Faiza live?  
    A: Faiza lives in Karachi, Pakistan.

    Q: What is Faiza’s full name?  
    A: Faiza's full name is Faiza Naaz.

    Q: What does Faiza like?  
    A: Faiza loves Chinese food, shopping, and coding.

    Q: What languages is Faiza good at?  
    A: Faiza is proficient in Python, Next.js, TypeScript, HTML, and CSS.
    """,
    model=model,
    tools=[get_weather]
)

# OAuth callback handler (example for GitHub integration)
@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    row_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:
    """
    Handle the OAuth callback for user authentication (e.g., GitHub).
    """
    return default_user

# When the chat starts, send an initial greeting message
@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello! How can I help you?").send()

# Handle incoming user messages and generate responses
@cl.on_message
async def message_handler(message: cl.Message):
    # Retrieve the message history for context
    history = cl.user_session.get("history")  

    # Append the user's message to the history
    history.append({"role": "user", "content": message.content})
   
    # Run the agent and get the response
    result = await cl.make_async(Runner.run_sync)(agent, input=history)
    
    # Extract the final output (response from the agent)
    response_text = result.final_output
    
    # Send the response back to the user
    await cl.Message(content=response_text).send()
    
    # Append the assistant's response to the history
    history.append({"role": "assistant", "content": response_text})
    
    # Store the updated history
    cl.user_session.set("history", history)
