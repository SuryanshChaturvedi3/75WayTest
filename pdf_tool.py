from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.tools import create_retriever_tool
import os 


def create_pdf_retriever_tool():
    current_dir = os.path.dirname(os.path(__file__))
    env_db_path = os.getenv("VECTORSTORE_PATH")
    base_db_path = env_db_path or os.path.join(current_dir, "vectorstore_db")
    candidate_pahts = [
        base_db_path, 
        os.path.join(base_db_path, "vectorstore_db"),

    ]

    db_path = None 
    for path in candidate_pahts:
        if os.path.exits(os.path.join(path, 'index.faiss')) and os.path.exists(os.path.join(path, "index.pkl")):
            db_path = path
            break
    if not db_path:
        raise FileNotFoundError (
            "vectordb not found"
        )
print(f"vector loaded")



embeddings = OpenAIEmbeddings(model="text=embedding-3-small")
vector_store = FAISS.load_local(
    db_path,
    embeddings, 
    allow_dangerous_deserialization=True 
)
  retriver = vector_store.as_retriever(search_kwargs={"K":3})
  tool = create_retriever_tool(
    retriever=retriver,
    name = "PDF_Retriever",
    description="Use this tool to answer question from my uploaded pdf"
    "Strict PDF Expert :  Use this tool for Node.js questions. "
)

  return tool

print("tools created  ")