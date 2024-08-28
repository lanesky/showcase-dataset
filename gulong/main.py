import os
from openai import OpenAI

# ============================
# Note: don't forget to set openai api key in the environment variable, refer to https://platform.openai.com/docs/quickstart/create-and-export-an-api-key
# ============================                                                s

client = OpenAI()

sytem_prompt = "你是古龙风格的chatbot。"
message_cache = [{
        "role": "system",
        "content": [
          {
            "type": "text",
            "text": sytem_prompt
          }
        ]
      },]

def chat_with_gpt(user_prompt):
  global message_cache

  message_cache.append({
    "role": "user",
    "content": [
      {
        "type": "text",
        "text": user_prompt
      }
    ]
  })

  response = client.chat.completions.create(
    model="ft:gpt-4o-mini-2024-07-18:aispin:gulong-style:A0zJeIqR",
    messages=message_cache,
    temperature=1.0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={
      "type": "text"
    }
  )

  assistant_response = response.choices[0].message.content  
  message_cache.append({
    "role": "assistant",
    "content": [
      {
        "type": "text",
        "text": assistant_response
      }
    ]
  })

  return assistant_response


# Example usage
if __name__ == "__main__":
  while True:
    user_prompt = input("User: ")
    assistant_response = chat_with_gpt(user_prompt)
    print("Assistant:", assistant_response)