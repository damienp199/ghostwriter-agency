from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class SeniorCopywriterAgent(Agent):
    def __init__(self):
        super().__init__(
            name="SeniorCopywriterAgent",
            description="Responsible for generating video titles, creating concise three-word titles for thumbnails, and selecting calls to action from a predefined list within the YouTube Ghostwriter Agency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            #tools=[CodeInterpreter],
            tools_folder="./tools",
            temperature=0.7,
            max_prompt_tokens=25000,
            model="gpt-4o",
        )
        
    def response_validator(self, message):
        return message
