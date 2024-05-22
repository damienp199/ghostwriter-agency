from openai import OpenAI
from rich import print

client = OpenAI()

assistant_id = "asst_ctI63UzgPMTXoUHWF5m8NzeR"
thread_id = "thread_4xXOONmZ6AakVsNWb5AT4k07"

# create a message
message = client.beta.threads.messages.create(
  thread_id=thread_id,
  role="user",
  content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

# create a run
run = client.beta.threads.runs.create_and_poll(
  thread_id=thread_id,
  assistant_id=assistant_id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

# delay for 30 seconds
#import time
#time.sleep(30)

import re

# check if the run is completed
if run.status == 'completed': 
    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )

    # Extract the necessary information from the messages
    for msg in messages.data:
        # Replace LaTeX equations with placeholder text
        text = msg.content[0].text.value
        text = re.sub(r'\\\(.*?\\\)', 'equation', text)
        text = re.sub(r'\\\[.*?\\\]', 'equation', text)

        print(f"[bold cyan]{msg.role}[/bold cyan]: {text}")
else:
    print(run.status)