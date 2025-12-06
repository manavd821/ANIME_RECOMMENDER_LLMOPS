from dataclasses import dataclass
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableLambda, RunnableParallel
from config.config import MODEL_NAME
from src.prompt_template import get_anime_prompt
from src.vector_store import VectorStore

@dataclass
class AnimeRecommender(VectorStore):
    llm = ChatGoogleGenerativeAI(
        model = MODEL_NAME
    )
    prompt = get_anime_prompt()
    
    @property
    def retriever(self):
        return self.load_vector_store().as_retriever()
    
    def get_recommandation(self, query : str):
        relevant_context_docs = self.retriever.invoke(query)
        relevant_context = "\n\n".join(doc.page_content for doc in relevant_context_docs)
        final_prompt = self.prompt.invoke({
            "context" : relevant_context, 
            "question" : query,
        })
        result = self.llm.invoke(final_prompt)
        return result.text