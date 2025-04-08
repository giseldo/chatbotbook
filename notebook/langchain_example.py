from langchain.chat_models import init_chat_model
import os

OPENAI_API_KEY =  os.environ.get("OPENAI_API_KEY"):

model = init_chat_model("gpt-4o-mini", model_provider="openai", openai_api_key=OPENAI_API_KEY)

response = model.invoke([
  {"role":"user", "content": "quem é o presidente do Brasil?"}
])

print(response.content)

