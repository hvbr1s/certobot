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
    Make sure to always cite your sources by adding a plain URL link.
    NEVER use markdown when sharing url links, always use plain text  instead.

    """
  ),
  expected_output="A detailed summary of the solution and the URL link to the relevant documentation that answers: '{topic}'",
  agent=researcher,
  async_execution=False,
)
