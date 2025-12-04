from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="data/index",
    embedding_function=embedding_model
)

retriever = db.as_retriever(search_kwargs={"k": 3})

def search_policy_docs(query: str) -> str:
    docs = retriever.get_relevant_documents(query)
    answer = ""
    for doc in docs:
        answer += doc.page_content[:800] + "\n"
        answer += f"source: {doc.metadata['source']}\n\n"
    return answer

app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.post("/ask")
def ask(input: QueryInput):
    response = search_policy_docs(input.query)
    return {"answer": response}
