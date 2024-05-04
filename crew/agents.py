import os
from crewai import Agent
from tools.retrieve_tool import retriever_tool
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import main

main.load_dotenv()

# Initialize LLms
gpt = ChatOpenAI(
    model="gpt-4-turbo",
    temperature=0.0
)
groq =  ChatGroq(
            api_key=os.environ['GROQ_API_KEY'],
            model="llama3-70b-8192"
)

# Creating a senior researcher agent with memory and verbose mode
researcher = Agent(
  role='Senior Researcher',
  goal='ALWAYS use your Knowledge Base tools to find solutions to technical questions about Ledger products.',
  verbose=True,
  memory=False,
  backstory=(
    """
      Driven by curiosity, you're at the forefront of cybersecurity applied to blockchain and an expert in Certora products including the Prover and Gambit.
      
    """
  ),
  tools=[retriever_tool],
  allow_delegation=False,
  llm=gpt,
  max_iter=10,
)

#For more information, ALWAYS direct the customer to the official Ledger store (https://shop.ledger.com/) or the Ledger Academy (https://www.ledger.com/academy) when appropriate.