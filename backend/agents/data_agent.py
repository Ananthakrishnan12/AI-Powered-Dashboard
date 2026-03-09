from crewai import Agent
from backend.llm_config import llm


data_agents = Agent(
    role="Dataset Understanding Expert",
    goal="Understand dataset structure and identify important columns",
    backstory="Expert data Analyst skilled in Understanding structured datasets",
    llm=llm,
    verbose=True,
)


analysics_agent = Agent(
    role="Buisness data Analyst",
    goal="Generate insights and identify trends in the dataset",
    backstory="Expert in extracting buisness insights from data",
    llm=llm,
    verbose=True,
)


visulization_agent=Agent(
    role="Data visulization specialist",
    goal="Recommend best charts for the dataset",
    backstory="Expert in desigining Analytical dashboards",
    llm=llm,
    verbose=True,
)