from dataclasses import dataclass
import pandas as pd

@dataclass
class AnimeDataLoader:
    original_csv : str
    processed_csv : str
    
    def load_and_process(self):
        data_frame = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines = 'skip').dropna()
        
        required_cols = {'Name' , 'Genres','sypnopsis'}
        
        missing = required_cols - set(data_frame.columns)
        if missing:
            raise ValueError("Missing columns ", *missing)
        
        data_frame['combine_info'] = (
            "Title: " + data_frame["Name"] + " Overview: " +data_frame["sypnopsis"] + "Genres : " + data_frame["Genres"]
        )
        
        data_frame[['combine_info']].to_csv(self.processed_csv, encoding='utf-8', index=False)
        
        return self.processed_csv