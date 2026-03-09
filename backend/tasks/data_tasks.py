from crewai import Task
from backend.agents.data_agent import data_agents ,analysics_agent,visulization_agent


data_task=Task(
    description="""Analyze the dataset structure.
                   Identify numerical columns, categorical columns 
                   and possible KPI's""",

    expected_output="""
    A clear description of dataset structure including:
    - numerical columns
    - categorical columns
    - possible KPIs
    """,

    agent=data_agents,
)

analytical_task=Task(
    description="""Analyze the dataset and generate key Insights,trends.""",

    expected_output="""
    A list of key insights, patterns and trends discovered in the dataset.
    """,

    agent=analysics_agent
)


