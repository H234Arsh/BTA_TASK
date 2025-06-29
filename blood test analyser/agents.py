from langchain_openai import ChatOpenAI
from crewai import Agent
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

# Securely load your OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Ensure the key is loaded
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not found.")

# Initialize the language model
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=openai_api_key
)

# Create doctor agent
doctor = Agent(
    role="AI Doctor",
    goal="Analyze blood test data and provide actionable insights",
    backstory="An expert doctor bot that interprets patient blood test results.",
    llm=llm
)

# Optional verifier agent
verifier = Agent(
    role="Data Verifier",
    goal="Ensure the medical insights are accurate and verified",
    backstory="Assists the doctor in checking report consistency.",
    llm=llm
)
