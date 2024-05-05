#%%
from pathlib import Path
import os

# Import functions from other scripts 
from configurations import basic_configurations
from formatting import formatting #definition_field, notes_field
from furigana import add_furigana
from deck import generate_anki_deck, export_df
from gpt import create_ai_prompts, handle_API_errors, get_ai_response

api_key = os.environ.get("OPENAI_API_KEY")
print("API_Key:", api_key)

def main():

    df, config_yaml, merged = basic_configurations(config_yaml_path, csv_file_path)
    print(df.head())

    prompts_df = create_ai_prompts(df, merged, config_yaml)
    
    handle_API_errors(get_ai_response, df, prompts_df)
    
    formatting(df, config_yaml)
    
    df = df.map(lambda x: add_furigana(x) if isinstance(x, str) else x)

    package = generate_anki_deck(df)  # Ensure this function accepts the dataframe and processes it accordingly

    export_df(df, config_yaml, package)
    
    return package, df

if __name__ == "__main__":
    # Choose the files to be used
    config_yaml_path = Path("config/config.yaml")
    csv_file_path = Path("test_dataframes/jn_items.csv")

    main()
# %%
