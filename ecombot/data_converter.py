import pandas as pd
from langchain_core.documents import Document

def data_converter():

    file_path = r"D:\learning\ETE_E_com_chatbot\data\flipkart_product_review.csv"

    data = pd.read_csv(file_path)

    data = data[["product_title","review"]]

    product_list = []
    for index,rows in data.iterrows():
        obj = {"product_name":rows["product_title"],"review":rows["review"]}
        product_list.append(obj)

    docs = []
    for pr in product_list:
        metadata = {"product_name":pr["product_name"]}
        doc = Document(page_content=pr["review"],metadata=metadata)
        docs.append(doc)

    return docs

