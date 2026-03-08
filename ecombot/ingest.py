from langchain_astradb import AstraDBVectorStore
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os
import pandas as pd
from langchain_huggingface import HuggingFaceEmbeddings
from ecombot.data_converter import data_converter

load_dotenv()

ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

def ingestion(status):
    # vstore = AstraDBVectorStore(
    #     collection_name="ecombot",
    #     embedding=embedding,
    #     api_endpoint=ASTRA_DB_API_ENDPOINT,
    #     token=ASTRA_DB_APPLICATION_TOKEN,
    #     namespace=ASTRA_DB_KEYSPACE,
    # )

    # storage = status

    # if storage == None:
    #     docs = data_converter()
    #     inserted_ids = vstore.add_documents(docs)
    # else:
    #     return vstore
    # return vstore, inserted_ids

# if __name__ == '__main__':
#     vstore, inserted_ids = ingestion(None)
#     print(f"\Inserted {len(inserted_ids)} documents.")
#     results = vstore.similarity_search("can you tell me the best bluetooth buds?")
#     for res in results:
#         print(f"* {res.page_content}[{res.metadata}]")