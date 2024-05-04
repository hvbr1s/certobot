from crewai import Task
from crew.agents import researcher

# Research task
research_issue= Task(
  description=(
    """
    Use your Knowledge base tool to find the best answer to: '{topic}'.
    ALWAYS use your Knowledge Base tool to answer the question asked: '{topic}'.
    After using your tool, assess if the information retrieved can correctly answer this question: '{topic}'. 
    If it does not answer the question, use your tool again until you find the answer.
    Make sure to always cite your sources by adding a plain URL link (no markdown).

    """
  ),
  expected_output="A detailed summary of the solution and the URL link to the relevant documentation that answers: '{topic}'",
  agent=researcher,
  async_execution=False,
)



    # A SHORT answer to this question: '{topic}'. Your answer MUST be friendly and engaging but ALWAYS be 3 sentences or less. 
    # Use the provided documentation to inform your response.
    # For more information, ALWAYS direct the customer to the official Ledger resources. Encourage visiting the Ledger store at https://shop.ledger.com/ for product purchases and the Ledger Academy at https://www.ledger.com/academy for educational content. 
    # ALWAYS insert a line break before directing the customer to the Ledger store or Ledger Academy.