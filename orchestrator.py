import os
import pandas as pd
import json
from dotenv import load_dotenv
import openai
import pandas as pd
import numpy as np
from pathlib import Path

# Import functions from other scripts 
from formatting import general_formatting, definition_field, notes_field
from furigana import add_furigana
from deck import generate_anki_deck
from gpt import create_df_messages, generate_content

# Load the environment variables
api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = api_key
print(api_key)

def main(df, config_json):

    # drop all rows where word_or_phrase is phrase
    df = df[df['word_or_phrase'] != 'Phrase']
    
    df_messages = create_df_messages(df, config_json)
    # print(df_messages)

    error_count = 0
    rows_to_delete = []  # List to store the indices of rows to be deleted

    for idx, row in df_messages.iterrows():
        for column in df_messages.columns:
            try:
                df.at[idx, column] = generate_content(row[column])
                error_count = 0  # Reset error count on success
            except Exception as e:
                error_count += 1
                if error_count >= 3:
                    rows_to_delete.append(idx)  # Add the index of the current row to the list
                    break  # Exit the inner loop to move to the next row

    if error_count < 3:  # Check for overall success after the loop
        # Delete the rows from the DataFrame
        df = df.drop(rows_to_delete)
        general_formatting(df_messages, config_json)
    
    

    
    # Apply formatting functions, general formatting: adding fields (so that the df is processed correctly), cloze pattern, hint, id, mp3, image
    general_formatting(df, config_json)

    # apply the other formatting for definition and notes field
    df["notes"] = df.apply(lambda row: notes_field(row["human_translation"], row["word_translation"]), axis=1)
    df["definition"] = df.apply(lambda row: definition_field(row["definition"], row["explanation"], row["grammar"], row["conjugation"], row["first_example"], row["second_example"]), axis=1)

    df = df.map(lambda x: add_furigana(x) if isinstance(x, str) else x)

    # Generate Anki deck
    package = generate_anki_deck(df)  # Ensure this function accepts the dataframe and processes it accordingly

    # save the deck to desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    package_path = os.path.join(desktop_path, f'{config_json["language"]}2{config_json["native_language"]}_LLN.apkg')
    package.write_to_file(package_path)

    print(f'Anki package "{package_path}" has been created.')

    # only keep the created fields, that should be displayed on the index.html
    # df = df[["synonyms", "hint", "first_example", "second_example", "explanation", "cloze", "definition", "image", "audio"]]
    df = df[["synonyms", "hint", "first_example", "second_example", "explanation", "cloze", "definition"]]
    # Replace empty strings with NaN
    df = df.replace('', np.nan)
    # Drop columns that only contain NaN
    df = df.dropna(how='all', axis=1)

    return df

if __name__ == "__main__":

    json_file_path = '/Users/moritzvitt/LR2Anki/config/ger_config.json'
    csv_file_path = '/Users/moritzvitt/LR2Anki/test_dataframes/ger_items.csv'

    # Open the JSON file and load its contents into a Python dictionary
    with open(json_file_path, 'r') as json_file:
        config_json = json.load(json_file)
    
    column_names = config_json['column_names']
    df = pd.read_csv(csv_file_path, delimiter='\t', names=column_names)
    print(column_names)
    # native_language column
    df['native_language'] = config_json['native_language']

    main(df, config_json)
# %%
