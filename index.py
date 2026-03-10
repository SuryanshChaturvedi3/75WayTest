from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()
import os


file_path ="./data.Pradhan Mantri Bhartiya Jan Aushadhi Pariyojna.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap=400)
splits = text_splitter.split_documents(docs)
embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")

vector_store = FAISS.from_documents(splits, embeddings)
vector_store.save_local("Medical_Voice_Agent/vectorstore_db")

print("PDF LOAd success")