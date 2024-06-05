#%%
from pathlib import Path
import yaml
import pandas as pd
import os
import json


# Import functions from other scripts 
from deck import formatting, generate_anki_deck, export_df
from config import config, column_names, log_io

class BaseAnkiDeckGenerator:
    def __init__(self, df: pd.DataFrame):
        self.ai_input_df = self.df[['short_phrase', 'short_translation', 'word']]


    # @log_io
    # def generate(self):
        
    #     prompts_df = create_ai_prompts(df=self.df, merged=self.merged_messages, config=self.config)
    #     handle_API_errors(get_ai_response, self.df, prompts_df)
    #     return self.df
    
    # def formatting(self):

    # def generate_anki_package(self):
    #     self.package = generate_anki_deck(self.df)
    #     return self.package
    
    
if __name__ == "__main__":
    csv_file_path = Path("test_dataframes/jn_items.csv")
    df = pd.read_csv(csv_file_path, delimiter='\t')

    # Determine the source of the DataFrame and create an instance of the appropriate class
    if 'items' in csv_file_path.stem:
        generator = BaseAnkiDeckGenerator(df, "Japanese")
    elif 'japanese_io' in csv_file_path.stem:
        generator = handle_japanese_io_df(df, config)
    elif 'kindle_exports' in csv_file_path.stem:
        generator = handle_kindle_exports_df(df, config)
    else:
        raise ValueError(f"Unknown source: {csv_file_path.stem}")

    package, df = generator.generate()

    output_file_path = os.path.join(os.path.expanduser("~"), "src", "LR2Anki", "downloads")
    export_df(df=df, package=package, native_language = config['native_language'], output_file_path=output_file_path)