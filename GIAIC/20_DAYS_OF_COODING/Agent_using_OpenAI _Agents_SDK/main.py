import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

# Fix the typo here
agent = Agent(
    name="Greeting Agent",
    instructions="You are a greeting agent, your task is to greet the user in a friendly manner. If anyone speaks 'hi', you respond with 'salam'.",
    model=model
)

user_question = input("Please enter your question: ")

# Assuming 'Runner.run_async' works as expected, using it to get the result
result = Runner.run_sync(agent, user_question)

# Print the result
print(result.final_output)
