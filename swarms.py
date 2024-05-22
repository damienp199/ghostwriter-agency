from agency_swarm import set_openai_key
from dotenv import load_dotenv
import os

load_dotenv()
set_openai_key(os.getenv("OPENAI_API_KEY"))


# Tools
from agency_swarm.tools import BaseTool
from pydantic import Field

class MyCustomTool(BaseTool):
    """
    A brief description of what the custom tool does. 
    The docstring should clearly explain the tool's purpose and functionality.
    """

    # Define the fields with descriptions using Pydantic Field
    example_field: str = Field(
        ..., description="Description of the example field, explaining its purpose and usage."
    )

    # Additional fields as required
    # ...

    def do_something(self, example_field: str):
        """
        A helper method to perform some task.
        This method should be used within the run method to perform the tool's operation.
        Doc string description is not required for this method.
        """

        # Your custom logic goes here
        return example_field

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform its task.
        Doc string description is not required for this method.
        """

        # Your custom tool logic goes here
        result = self.do_something(self.example_field)

        # Return the result of the tool's operation
        return result
    

from agency_swarm import Agent

ceo = Agent(name="CEO",
            description="Responsible for client communication, task planning and management.",
            instructions="You must converse with other agents to ensure complete task execution.", # can be a file like ./instructions.md
            #files_folder="./files", # files to be uploaded to OpenAI
            #schemas_folder="./schemas", # OpenAPI schemas to be converted into tools
            tools=[MyCustomTool], 
            temperature=0.5, # temperature for the agent
            max_prompt_tokens=25000, # max tokens in conversation history
            )

dev = Agent(name="Developer",
            description="Responsible for developing software solutions and implementing client requirements.",
            instructions="You must develop what we told you.",
            #files_folder="./files", # files to be uploaded to OpenAI
            #schemas_folder="./schemas", # OpenAPI schemas to be converted into tools
            #tools=[MyCustomTool], 
            temperature=0.5, # temperature for the agent
            max_prompt_tokens=25000, # max tokens in conversation history
            )

from agency_swarm import Agency

agency = Agency([
       ceo,  # CEO will be the entry point for communication with the user
       [ceo, dev],  # CEO can initiate communication with Developer
     ], 
     shared_instructions='agency_manifesto.md', #shared instructions for all agents
     temperature=0.5, # default temperature for all agents
     max_prompt_tokens=25000 # default max tokens in conversation history
)


agency.run_demo()