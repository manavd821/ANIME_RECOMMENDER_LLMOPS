from dataclasses import dataclass

from sympy import EX
from src.recommender import AnimeRecommender
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

@dataclass
class AnimeRecommenderPipeline:
    persist_dir = "chroma_db"
    
    try:
        logger.info("Initializing Recommendation Pipeline...")
        recommender = AnimeRecommender(csv_path="", persist_dir = persist_dir)
        logger.info("Pipleine intialized successfully...")

    except Exception as e:
        logger.error(f"Failed to intialize pipeline {str(e)}")
        raise CustomException("Error during pipeline intialization" , e)

    def recommend(self, query : str):
        try:
            logger.info(f"Recived a query {query}")
            
            recommendation = self.recommender.get_recommandation(query)
            
            logger.info("Recommendation generated successfully...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during recommendation" , e)
    
