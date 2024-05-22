from openai import OpenAI

client = OpenAI()

thread = client.beta.threads.create()

print(thread)


