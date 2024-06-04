#%%
from pathlib import Path
import yaml
import pandas as pd
import os
import json


# Import functions from other scripts 
from deck import formatting, generate_anki_deck, export_df
from gpt import create_ai_prompts, handle_API_errors, get_ai_response
from config import config, column_names, log_io

class BaseAnkiDeckGenerator:
    def __init__(self, df: pd.DataFrame, config: dict):
        self.df = df
        self.config = config
        self.wanted_fields = config['wanted_fields']

        self.target_language = config['target_language']
        self.native_language = config['native_language']
        self.load_config_files()

        self.prepare_data()
        self.merged_messages()


    def load_config_files(self):
        with open('config/messages.yaml', 'r') as file:
            self.messages_yaml = yaml.safe_load(file)

        with open('config/examples.yaml', 'r') as file:
            self.examples_yaml = yaml.safe_load(file)

        with open('/config/language_codes.json', 'r') as file:
            self.language_codes = json.load(file)    

    def prepare_data(self):
        if config['target_language'] == None:
            self.df['target_language'] = self.df['target_language'].map(self.language_codes)

        if config['native_langugae'] == None:
            self.df['native_language'] = self.df['native_language'].map(self.language_codes)

        # dataframe to send to chatGPT
        # columns to keep in the new pandas_dataframe: short_phrase, short_translation, word
        self.ai_input_df = self.df[['short_phrase', 'short_translation', 'word']]
        return self.ai_input_df
    
    def merged_messages(self):
        # Extract the examples for the target language
        target_language_examples = self.examples.get(self.target_language, {})

        # Merge the messages and target language examples dictionaries
        merged = {
            key: self.messages.get(key, '') + ' ' + target_language_examples.get(key, '')
            for key in set(self.messages) | set(target_language_examples)
        }

        return merged

    @log_io
    def generate(self):
        
        prompts_df = create_ai_prompts(df=self.df, merged=self.merged_messages, config=self.config)
        handle_API_errors(get_ai_response, self.df, prompts_df)
        formatting(self.df, self.config)
        return self.df
    
    def generate_anki_package(self):
        self.package = generate_anki_deck(self.df)
        return self.package
    
class handle_language_reactor_df(BaseAnkiDeckGenerator):
    def prepare_data(self):
        self.df.columns = column_names
        super().prepare_data()

class handle_japanese_io_df(BaseAnkiDeckGenerator):
    def __init__(self, df: pd.DataFrame, config: dict):
        super().__init__(df, config)
        self.target_language = 'japanese'

    def prepare_data(self):
        super().prepare_data()
        # Perform additional processing specific to handle_japanese_io_df
        pass

class handle_kindle_exports_df(BaseAnkiDeckGenerator):
    def prepare_data(self):
        super().prepare_data()
        # Perform additional processing specific to handle_kindle_exports_df
        pass
    
if __name__ == "__main__":
    csv_file_path = Path("test_dataframes/jn_items.csv")
    df = pd.read_csv(csv_file_path, delimiter='\t')

    # Determine the source of the DataFrame and create an instance of the appropriate class
    if 'items' in csv_file_path.stem:
        generator = handle_language_reactor_df(df, config)
    elif 'japanese_io' in csv_file_path.stem:
        generator = handle_japanese_io_df(df, config)
    elif 'kindle_exports' in csv_file_path.stem:
        generator = handle_kindle_exports_df(df, config)
    else:
        raise ValueError(f"Unknown source: {csv_file_path.stem}")

    package, df = generator.generate()

    output_file_path = os.path.join(os.path.expanduser("~"), "src", "LR2Anki", "downloads")
    export_df(df=df, package=package, native_language = config['native_language'], output_file_path=output_file_path)