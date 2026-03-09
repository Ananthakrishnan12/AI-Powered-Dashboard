from crewai import Crew

from backend.agents.data_agent import data_agents ,analysics_agent,visulization_agent
from backend.tasks.data_tasks import data_task,analytical_task



def run_ai_analysis():
    crew=Crew(
        agents=[
            data_agents ,
            analysics_agent,
            visulization_agent
        ],

        tasks=[
            data_task,
            analytical_task
        ],
        verbose=True
    )


    result=crew.kickoff()

    return result