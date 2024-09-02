import os.path
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from llama_index.core import Settings

# 设置 OpenAI Embedding 模型，这里使用了 text-embedding-3-small 模型
Settings.embed_model = OpenAIEmbedding(
    model_name="text-embedding-3-small"
)
# 设置 OpenAI 模型，这里使用了 gpt-4o-mini 模型
Settings.llm = OpenAI(model="gpt-4o-mini")

# 设置持久化目录，用来存储索引
PERSIST_DIR = "./storage"

# 如果持久化目录不存在，则创建索引
if not os.path.exists(PERSIST_DIR):
    # 遍历 novel 目录下的文档，加载数据，创建索引
    documents = SimpleDirectoryReader("novel").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # 持久化索引，存储到 PERSIST_DIR 目录，方便下次加载
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # 如果持久化目录存在，则从持久化目录加载索引
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# 使用索引进行查询
query_engine = index.as_query_engine()
response = query_engine.query("这篇故事的主题讲的是什么？")
print(response)