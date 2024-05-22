#%%
from pathlib import Path
import yaml
import pandas as pd
import os

# Import functions from other scripts 
from logging_config import logger, log_io
from configurations import basic_configurations
from formatting import formatting #definition_field, notes_field
from furigana import add_furigana
from deck import generate_anki_deck, export_df
from gpt import create_ai_prompts, handle_API_errors, get_ai_response



@log_io
# TODO main should accept a df over 50 rows long
def main(df, config):

    # Load all configuration files
    with open('config/column_names.yaml', 'r') as file:
        data = yaml.safe_load(file)
        column_names = data['column_names']

    with open('config/messages.yaml', 'r') as file:
        messages_yaml = yaml.safe_load(file)

    with open('config/examples.yaml', 'r') as file:
        examples_yaml = yaml.safe_load(file)

    # TODO target_langugage default value should come from df, 
    # only if user decides to set a different one, take the value from the config

    df, merged_messages = basic_configurations(df=df, 
                                      target_language=config['target_language'], 
                                      native_language=config['native_language'], 
                                      column_names=column_names, 
                                      messages=messages_yaml, 
                                      examples=examples_yaml
                                    )

    prompts_df = create_ai_prompts(df, merged=merged_messages, config=config)
    handle_API_errors(get_ai_response, df, prompts_df)
    
    formatting(df, config)
    
    df = df.map(lambda x: add_furigana(x) if isinstance(x, str) else x)
    logger.info(f"Dataframe after furigana: {df.head()}")

    package = generate_anki_deck(df)  # Ensure this function accepts the dataframe and processes it accordingly

    return package, df
    
if __name__ == "__main__":
    # Choose the files to be used
    config_path = Path("config/config.yaml")
    csv_file_path = Path("test_dataframes/jn_items.csv")

    #safe variables 'native_language' and 'target_language' 
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Load the csv file
    df = pd.read_csv(csv_file_path, delimiter='\t')
    
    package, df = main(df, config)

    output_file_path = os.path.join(os.path.expanduser("~"), "src", "LR2Anki", "downloads")
    export_df(df=df, package=package, native_language = config['native_language'], output_file_path=output_file_path)
# %%
