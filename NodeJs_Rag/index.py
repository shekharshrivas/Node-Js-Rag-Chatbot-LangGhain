from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

pdf_path = Path(__file__).parent / "NodeJs.pdf"

# Load the PDF document
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# Split the document into smaller chunks
text_spliter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400)

chunks = text_spliter.split_documents(documents=docs)

# vector embedding
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)


vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="nodejs-docs",
    url="http://localhost:6333"
)


print("Indexing of the document done ...")
