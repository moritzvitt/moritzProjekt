#%%
from pathlib import Path
import yaml
import pandas as pd
import os

# Import functions from other scripts 
from configurations import basic_configurations
from formatting import formatting #definition_field, notes_field
from furigana import add_furigana
from deck import generate_anki_deck, export_df
from gpt import create_ai_prompts, handle_API_errors, get_ai_response

def main(df, config):
    
    df, merged = basic_configurations(df, config)

    prompts_df = create_ai_prompts(df, merged, config)
    handle_API_errors(get_ai_response, df, prompts_df)
    
    formatting(df, config)
    
    df = df.map(lambda x: add_furigana(x) if isinstance(x, str) else x)

    package = generate_anki_deck(df)  # Ensure this function accepts the dataframe and processes it accordingly

    return package, df
    
if __name__ == "__main__":
    # Choose the files to be used
    config_path = Path("config/config.yaml")
    csv_file_path = Path("test_dataframes/jn_items.csv")

    #safe variables 'native_language' and 'target_language' 
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        column_names = config['column_names']

    # Load the csv file
    df = pd.read_csv(csv_file_path, delimiter='\t')
    
    package, df = main(df, config)

    output_file_path = os.path.join(os.path.expanduser("~"), "Desktop")
    export_df(df, package, config, output_file_path)
# %%
