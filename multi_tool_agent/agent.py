from google.adk.agents import LlmAgent
from google.adk.tools import google_search

MODEL = "gemini-2.0-flash-exp"

idea_agent = LlmAgent(
    model=MODEL,
    name="IdeaAgent",
    description="An agent specialized in brainstorming creative and innovative ideas based on user requests.",
    instruction="You are an experienced software engineer, Use the tool to brainstorm and reposnd to the user with 3 most relevant and actionable advices based on the user's request",
    tools=[google_search],
    disallow_transfer_to_peers=True,
)

refiner_agent = LlmAgent(
    model=MODEL,
    name="RefinerAgent",
    description="Reviews provided career advices and selects only those which are actionable and extimated to propel the career of a mew software engineer.",
    instruction="Use your tool to review the provided career advices. Respond ONLY with the advices which are actionable and can help the user grow in his/her sfotware development career, If nothing is availabe inform the user.",
    tools=[google_search],
    disallow_transfer_to_peers=True,
)

root_agent = LlmAgent(
    model=MODEL,
    name="PlannerAgent",
    instruction=f"""
    You are a Seasoned software engineer, coordinating specialist agents.
    Your goal is to provide relevant and actionable steps and mentorship to new Computer science students and junior engineers.
    For each user request, follow the below instructions.
    1. First, use "{idea_agent}" to brainstorm ideas based on user request.
    2. Then, use "{refiner_agent}" to take those ideas to filter them for the provided query.
    3. Present the final, refined list to the user along with the actionable steps.
    """,
    sub_agents=[idea_agent, refiner_agent],
)
