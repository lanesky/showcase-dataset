from openai import OpenAI
import numpy as np
import os

# 创建 OpenAI 客户端
client = OpenAI()

# 定义函数，计算两个向量的余弦相似度
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# 定义函数，使用 OpenAI API 将文本嵌入为向量
def embed_text(text):
    response = client.embeddings.create(input=[text], model="text-embedding-3-small")
    #print(f"Text: {text} \tEmbedding: {response.data[0].embedding}")
    return response.data[0].embedding
    
# 定义函数，加载文本文件并将每行文本嵌入为向量
def load_and_embed_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    embeddings = [embed_text(line.strip()) for line in lines]
    return lines, embeddings

# 定义函数，获取查询的文本嵌入
def get_query_embedding(query):
    return embed_text(query)

# 定义函数，搜索与查询文本最相似的文本
def search_text(query, lines, embeddings):
    # 获取查询文本的嵌入
    query_embedding = get_query_embedding(query)
    # 计算查询文本与所有文本的相似度
    similarities = [cosine_similarity(query_embedding, emb) for emb in embeddings]
    # 使用最大相似度的文本作为最佳匹配
    best_match_index = np.argmax(similarities)
    # 返回最佳匹配的文本和相似度
    return lines[best_match_index], similarities[best_match_index]


# 定义文件路径和查询
file_path = 'data/authors.txt'
query = "三国演义是谁写的"  

# 加载文本
lines, embeddings = load_and_embed_text(file_path)

# 搜索最相似的文本
best_match, similarity = search_text(query, lines, embeddings)

# 输出结果, 打印最相似的文本和相似度
print(f"Best match: {best_match}\nSimilarity: {similarity}")
