from crewai import Agent, Crew, Process
from tasks import Task
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the LLM (Azure OpenAI)
default_llm = AzureChatOpenAI(
    openai_api_version=os.getenv("AZURE_OPENAI_VERSION", "2023-12-01-preview"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gama"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", "https://ai-gamaai623587016894.openai.azure.com/"),
    api_key=os.getenv("AZURE_OPENAI_KEY")  # Fetch the key from .env
)

# Create a researcher agent
researcher = Agent(
    role='Senior Researcher',
    goal='Discover groundbreaking technologies',
    verbose=True,
    llm=default_llm,
    backstory='A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.'
)

# Define the task for the researcher
research_task = Task(
    description='Identify the next big trend in AI',
    agent=researcher,  # Assigning the task to the researcher
    expected_output="A detailed report on the next significant AI trend.",
    inputs={"data_sources": ["research papers", "tech blogs", "market analysis"]}
)

# Print the task to verify it's being created correctly
print("Task Initialized:", research_task)

# Create the crew (pass a list of Task objects)
try:
    tech_crew = Crew(
        agents=[researcher],
        tasks=[research_task],  # Ensure this is a list of Task objects
        process=Process.sequential  # Tasks will be executed one after the other
    )
    print("Crew Initialized:", tech_crew)
    
    # Start the task execution
    tech_crew.kickoff()

except Exception as e:
    print(f"An error occurred: {e}")
