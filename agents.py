from crewai import Agent
from llm.ollama_llm import llm

intent_agent = Agent(
    role="Intent Detection Agent",
    goal="Extract application, severity, and issue from support tickets",
    backstory="Expert in analyzing IT support issues.",
    llm=llm
)

routing_agent = Agent(
    role="Routing Agent",
    goal="Assign the ticket to the right support team and assess urgency",
    backstory="Expert in support routing and workload optimization.",
    llm=llm
)

kb_agent = Agent(
    role="Knowledge Base Agent",
    goal="Recommend a solution from known internal resolutions",
    backstory="Familiar with past resolutions and best practices.",
    llm=llm
)


intent_agent = Agent(
    role="Intent Detection Agent",
    goal="Extract application, severity, and issue from support tickets",
    backstory="Expert in analyzing IT support issues.",
    llm=llm
)

routing_agent = Agent(
    role="Routing Agent",
    goal="Assign the ticket to the right support team and assess urgency",
    backstory="Expert in support routing and workload optimization.",
    llm=llm
)

kb_agent = Agent(
    role="Knowledge Base Agent",
    goal="Recommend a solution from known internal resolutions",
    backstory="Familiar with past resolutions and best practices.",
    llm=llm
)
