from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import CharacterTextSplitter
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()
@dataclass
class VectorStore:
    csv_path : str
    persist_dir : str = "chroma_db"
    embedding = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
    )
    
    def build_and_save_vector_store(self):
        loader = CSVLoader(
            self.csv_path,
            encoding='utf-8',
            metadata_columns=[]
        )
        
        data = loader.load()
        
        splitter = CharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 0,
        )
        
        texts = splitter.split_documents(data)
        
        db = Chroma.from_documents(
            texts,
            embedding=self.embedding,
            persist_directory=self.persist_dir,
        )
        return db
        
        
    def load_vector_store(self):
        return Chroma(
            persist_directory=self.persist_dir,
            embedding_function=self.embedding,
        )