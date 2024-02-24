# %% [markdown]
# # Next TODO: 
# 
# I need a working deck, that I can learn with <b>as fast as possible!</b>
# 
# - <span style="color:lightgreen">Anki card styling!</span> Like 'the NewYorker' or 'Economist'! Black fonts, different sizes, like a newspaper! With thin lines between definition, hint, notes...
# - add <span style="color:lightgreen">『』, "" </span> to long_sentence for better styling
# - load <span style="color:lightgreen">"native_langage"</span> as a column and have a native_message for everything!  
# - <span style="color:lightgreen">ふりがな</span> with a python library, not in Anki. Apparently 'Sudachi' is very reliable... Mecab. (kodachi) Have <span style="color:lightgreen">furigana</span> in separate code!
# - maybe include a japanese dictionary like https://pypi.org/project/jamdict/ to improve the definitions. Which dictionaries should I rely on? API, downloaded html dictionary or something else? What does Lisardo say?
# 
# ## Wish list: 
# - more synonyms, always also in target_language
# - related phrases, common phrases....
# - create a gpt assistant that gives better definitions
# - more Kanji information
# Different information depending on word_type:
#     + nouns: related words, びょういん and 病気　etc,
#     + verbs: conjugation, て-Form! (to know if る or う), prepositions for the verbs...
#     + adjectives: な or い, conjugation examples
# 

# %%
import os
import pandas as pd
import json
from dotenv import load_dotenv
import openai
import os
import pandas as pd

# Import functions from other scripts 
from formatting import general_formatting, definition_field, notes_field
from furigana import add_furigana
from deck import generate_anki_deck
from gpt import create_df_messages, generate_content
import numpy as np

# chatGpt configuration
load_dotenv()
openai.api_key = os.getenv("22API_KEY")
ai_model = os.getenv("model")

def main(df, config_json):

    # drop all rows where word_or_phrase is phrase
    df = df[df['word_or_phrase'] != 'Phrase']
    
    df_messages = create_df_messages(df, config_json)
    # print(df_messages)

    error_count = 0  # Correctly initialized at the beginning
    for idx, row in df_messages.iterrows():
        if error_count >= 3:
            break  # Check at the beginning of the outer loop to avoid unnecessary iterations
        for column in df_messages.columns:
            try:
                df_messages.at[idx, column] = generate_content(row[column])
            except Exception as e:
                error_count += 1
                if error_count >= 3:
                    break  # Only breaks the inner loop, but already checked condition in the outer loop

    # if error_count < 3:
    #     # Continue with the rest of the code only if fewer than 3 errors occurred
    #     general_formatting(df_messages, config_json)
    #     # Rest of the code that depends on successful completion...


    
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

    json_file_path = '/Users/moritzvitt/coding/config/ger_config.json'
    csv_file_path = '/Users/moritzvitt/downloads/ger_example/items.csv'

    # Open the JSON file and load its contents into a Python dictionary
    with open(json_file_path, 'r') as json_file:
        config_json = json.load(json_file)
    
    column_names = config_json['column_names']
    df = pd.read_csv(csv_file_path, delimiter='\t', names=column_names)

    # native_language column
    df['native_language'] = config_json['native_language']

    main(df, config_json)
# %%
