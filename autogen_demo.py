from autogen import ConversableAgent

user = ConversableAgent(
    name='User',
    llm_config=False,
    human_input_mode='NEVER'
)
assistant = ConversableAgent(
    name='PythonAssistant',
    llm_config={'model': 'gpt-4o-mini'}
)
user.initiate_chat(
    assistant,
    message='Write a Python script that monitors my Downloads folder and auto-sorts files by type.'
)