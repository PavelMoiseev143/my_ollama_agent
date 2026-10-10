
from ollama import chat

response = chat(
    model='qwen3',
    messages=[{'role': 'user', 'content': 'Привет, как тебя зовут, что ты умеешь?'}],
)
print(response.message.content)
