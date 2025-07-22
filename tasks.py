from crewai import Task


def get_tasks(ticket, agents):
    ticket_text = ticket["Ticket Text"]

    task1 = Task(
        description=(
            "Analyze the following IT support ticket and extract:\n"
            "- Application involved\n"
            "- Severity (Low, Medium, High)\n"
            "- Issue described\n\n"
            f"Ticket: {ticket_text}"
        ),
        expected_output="JSON with keys: application, severity, issue",
        output_format="json",
        agent=agents["intent"]
    )

    task2 = Task(
        description=(
            "Based on the previous task's application and issue, "
            "decide which IT support team should handle this ticket and assign urgency.\n"
            "Format: JSON with keys: team, urgency"
        ),
        expected_output="JSON with keys: team and urgency",
        output_format="json",
        agent=agents["routing"],
        context=[task1]
    )

    task3 = Task(
        description=(
            "Based on the previous intent analysis, provide a resolution from the internal knowledge base."
        ),
        expected_output="A sentence suggesting the resolution.",
        output_format="raw",
        agent=agents["kb"],
        context=[task1]
    )

    return [task1, task2, task3]
