from agency_swarm.agents import Agent


class SeniorCEOAgent(Agent):
    def __init__(self):
        super().__init__(
            name="SeniorCEOAgent",
            description="Acts as the primary point of contact for the user, coordinates with other agents, and oversees the entire operation within the YouTube Ghostwriter Agency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
            model="gpt-4o"
        )
        
    def response_validator(self, message):
        return message
