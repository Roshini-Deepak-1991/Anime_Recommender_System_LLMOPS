import streamlit as st
from pipeline.pipeline import AnimeRecommenderPipeline
from dotenv import load_dotenv


st.set_page_config(page_title = "Anime Recommender", layout = "wide")

load_dotenv()


@st.cache_resource
def init_pipeline():
    return AnimeRecommenderPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime preferences eg: light hearted anime with a happy ending")

if query:
    with st.spinner("Generating Anime Recommendation..."):
        recommendation = pipeline.recommend(query)
        st.markdown("Anime Recommendation")
        st.write(recommendation)




