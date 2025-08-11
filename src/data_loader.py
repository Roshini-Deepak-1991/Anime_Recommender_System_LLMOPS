import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_data_path:str, processed_data_path:str):
        self.original_data_path = original_data_path
        self.processed_data_path = processed_data_path

    def load_data_and_process(self):
        df = pd.read_csv(self.original_data_path, encoding = "utf-8", on_bad_lines= 'skip').dropna()
        # df.to_csv(self.processed_data_path, index=False)
        required_cols = {"Name" , "Genres" , "sypnopsis"}
        missing = required_cols - set(df.columns)

        # set(df.columns) meand 

        if missing:
            raise ValueError(f"Missing required columns: {', '.join(missing)}")
        
        df['combined_info'] = ( "Title: " + df["Name"] + " Genres: " + df["Genres"] + " Synopsis: " + df["sypnopsis"])
        
        df[['combined_info']].to_csv(self.processed_data_path, index=False, encoding = 'utf-8')

        return self.processed_data_path