# This will be used for our recommendation purpose

from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger  import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv


logger = get_logger(__name__)

class AnimeRecommenderPipeline:
    def __init__(self, persist_dir="chroma_db"):
        try:
            logger.info("Initializing Anime Recommender Pipeline")
            vector_builder = VectorStoreBuilder(csv_path = "" , persist_dir = persist_dir)
            retreiver = vector_builder.load_vector_store().as_retriever()
            # self.vector_store = VectorStoreBuilder(GROQ_API_KEY, MODEL_NAME)
            self.recommender = AnimeRecommender(retreiver , GROQ_API_KEY, MODEL_NAME)

        except Exception as e:
            logger.error(f"Error while initializing Anime Recommender Pipeline: {e}")
            raise CustomException("Error during pipeline initialization",e)
        
    def recommend(self, query:str) -> str:
        try:
            logger.info("Generating Anime Recommendation")
            recommendation = self.recommender.get_recommendation(query)
            return recommendation
        except Exception as e:
            logger.error(f"failed to get recommendation {str(e)}")
            raise CustomException("Error during pipeline initialization", e)


    