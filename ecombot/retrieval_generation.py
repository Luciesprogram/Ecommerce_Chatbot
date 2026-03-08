from langchain_core.output_parsers import StrOutputParser #takes the complex object which LLM returns and strip or remove everything including metadata except the actual text content.
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough #For runtime passing user message directly to retriever for finding relevant vectors and llm to what to give output without doing any changes in that.
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
from ecombot.ingest import ingestion
import torch

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 10})

    PRODUCT_BOT_TEMPLATE = """
        You are an ecommerce bot expert in different products recommendations to customer using the product_name and reviews.
        If the answer is not present, reply: "I could not find the answer in the provided details.".
        Identify the most relevant products question is asking and why these product will be good choice to them.
        Answer clearly in 200 words only.
        Do not use any external knowledge and stay on the topic.

    CONTEXT:
    {context}

    QUESTION:
    {question}


    
    """

    pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    max_new_tokens=300,
    temperature=0.1,
    do_sample=False,
)

    llm = HuggingFacePipeline(pipeline=pipe,model_kwargs={"stop": ["\n\n", "Human:", "Note:"]})

    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)


    chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    # | StrOutputParser()
)

    return chain


if __name__=='__main__':
    vstore = ingestion("done")
    chain  = generation(vstore)
    print(chain.invoke("can you tell me the best bluetooth buds?"))

