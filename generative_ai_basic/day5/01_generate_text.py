from openai import OpenAI
import os

# 创建 OpenAI 客户端
client = OpenAI()

# 设置对话
system_message = "我是一个友好的聊天机器人，我可以回答你的问题。"
user_message = "请告诉我一些关于黑神话悟空的事情"

# 生成文本
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages = [
      {"role":"system", "content": system_message},
      {"role":"user","content":user_message},],
  temperature=1,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "text"
  }
)

# 输出生成的文本
print(response.choices[0].message.content)