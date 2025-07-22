import pandas as pd
from crewai import Crew
from agents import intent_agent, routing_agent, kb_agent
from tasks import get_tasks
from pathlib import Path
import json

df = pd.read_excel("data/tickets.xlsx")
results = []

agents = {
    "intent": intent_agent,
    "routing": routing_agent,
    "kb": kb_agent
}

for _, ticket in df.iterrows():
    print(
        f"\n Processing ticket {ticket['Ticket ID']} - {ticket['Ticket Text']}\n")

    crew = Crew(
        agents=[intent_agent, routing_agent, kb_agent],
        tasks=get_tasks(ticket, agents),
        verbose=True
    )

    try:
        result = crew.kickoff()
        task1_output, task2_output, task3_output = result

        intent_data = json.loads(task1_output)
        routing_data = json.loads(task2_output)

        results.append({
            "Ticket ID": ticket["Ticket ID"],
            "User": ticket["User"],
            "Ticket Text": ticket["Ticket Text"],
            "Application": intent_data.get("application", "Unknown"),
            "Severity": intent_data.get("severity", "Unknown"),
            "Issue": intent_data.get("issue", "Unknown"),
            "Routing Decision": routing_data,
            "KB Suggestion": str(task3_output)
        })

    except Exception as e:
        print(" Error:", e)
        results.append({
            "Ticket ID": ticket["Ticket ID"],
            "User": ticket["User"],
            "Ticket Text": ticket["Ticket Text"],
            "Application": "Error",
            "Severity": "Error",
            "Issue": "Error",
            "Routing Decision": "Error",
            "KB Suggestion": str(e)
        })

Path("outputs").mkdir(exist_ok=True)
df_out = pd.DataFrame(results)
df_out.to_excel("outputs/ticket_results.xlsx", index=False)
print("\n Output saved to outputs/ticket_results.xlsx")
