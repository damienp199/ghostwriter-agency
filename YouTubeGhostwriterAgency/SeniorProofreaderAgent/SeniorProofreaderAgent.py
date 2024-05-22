from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class SeniorProofreaderAgent(Agent):
    def __init__(self):
        super().__init__(
            name="SeniorProofreaderAgent",
            description="Validates the generated content, ensures it aligns with YouTube guidelines, and builds tracking UTMs within the YouTube Ghostwriter Agency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
            model="gpt-4o",
        )
        
    def response_validator(self, message):
        return message
