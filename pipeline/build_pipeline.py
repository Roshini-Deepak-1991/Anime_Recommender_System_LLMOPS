# This will be used to create the vector store

from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger  import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("starting to build pipeline...")
        
        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_with_synopsis_processed.csv")

        processed_csv = loader.load_data_and_process()

        logger.info("Data loaded and processed")

        vector_builder = VectorStoreBuilder(csv_path = processed_csv, persist_dir = "chroma_db")

        vector_builder.build_and_save_vectorstore()

        logger.info("Vector store built and saved")

        logger.info("pipeline initiated succesfully")

    except Exception as e:
            logger.error(f"Error while initializing Anime Recommender Pipeline: {str(e)}")
            raise CustomException("Error during pipeline initialization",e)
    
if __name__ == "__main__":
    main()
        


