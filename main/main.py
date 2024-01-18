from openai import OpenAI
from skKey import API_KEY
client = OpenAI(api_key=API_KEY)

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo-1106"
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

messages = client.beta.threads.messages.list(
  thread_id=thread.id,
)


message = client.beta.threads.messages.retrieve(
  thread_id=thread.id,
)
print(message)
