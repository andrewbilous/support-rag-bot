import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import pipeline

load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
assert HF_TOKEN, "❌ Hugging Face token not found. Make sure it's in your .env file."

PDF_PATH = "support-policy.pdf"
LLM_MODEL = "tiiuae/falcon-rw-1b"
EMBED_MODEL = "thenlper/gte-small"

loader = PyPDFLoader(PDF_PATH)
docs = loader.load_and_split()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)


embedding = HuggingFaceEmbeddings(
    model_name=EMBED_MODEL,
    model_kwargs={"device": "cpu"} 
)
db = FAISS.from_documents(chunks, embedding)
retriever = db.as_retriever(search_type="similarity", k=3)


llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
