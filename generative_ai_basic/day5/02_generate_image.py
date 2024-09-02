from openai import OpenAI
import os

# 创建 OpenAI 客户端
client = OpenAI()

# 生成图片
response = client.images.generate(
  model="dall-e-2",
  prompt="一只白色的暹罗猫",
  size="1024x1024",
  quality="standard",
  n=1,
)

# 输出图片链接
image_url = response.data[0].url
print(image_url)