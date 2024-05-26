#%%
from pathlib import Path
import yaml
import pandas as pd
import os

# Import functions from other scripts 
from logging_config import log_io
from prepare_data import prepare_data, create_ai_prompts
from formatting import formatting #definition_field, notes_field
from deck import generate_anki_deck, export_df
from gpt import handle_API_errors, get_ai_response



@log_io
# TODO main should accept a df over 50 rows long
def main(df: pd.DataFrame, config: dict) -> tuple:

    with open('config/messages.yaml', 'r') as file:
        messages_yaml = yaml.safe_load(file)

    with open('config/examples.yaml', 'r') as file:
        examples_yaml = yaml.safe_load(file)



    df, merged_messages = prepare_data(df=df, 
                                      target_language=config['target_langauage'], 
                                      native_language=config['native_language'], 
                                      messages=messages_yaml, 
                                      examples=examples_yaml
                                    )

    prompts_df = create_ai_prompts(df, merged=merged_messages, config=config)

    handle_API_errors(get_ai_response, df, prompts_df)
    
    formatting(df, config)
    
    package = generate_anki_deck(df)  #Ensure this function accepts the dataframe and processes it accordingly
    
    return package, df
    
if __name__ == "__main__":
    from ..config.config import config

    csv_file_path = Path("test_dataframes/jn_items.csv")
    df = pd.read_csv(csv_file_path, delimiter='\t')
    
    package, df = main(df, config)

    output_file_path = os.path.join(os.path.expanduser("~"), "src", "LR2Anki", "downloads")
    export_df(df=df, package=package, native_language = config['native_language'], output_file_path=output_file_path)
# %%
