import genanki 
import numpy as np
import os
import time
from logging_config import logger, log_io

@log_io
def generate_anki_deck(df):
    with open('templates/anki_card.html', 'r', encoding='utf-8') as content_file:
        content = content_file.read()   

    # Splitting HTML content
    html_sections = content.split('<!-- html -->')

    # Assigning sections to qfmt, afmt, and css
    qfmt_html = html_sections[1]
    afmt_html = html_sections[2]

    with open('static/css/anki_card.css', 'r', encoding='utf-8') as content_file:
        css_code = content_file.read() 
    

    # df = df_anki[["ID", "cloze", "hint", "definition", "notes", "image", "audio"]]
    # so no problem later with the anki package, to string
    df = df.astype(str)

    # Define the Anki model
    model_id = 1607392319
    model = genanki.Model(
        model_id,
        'Language Learning with Netflix Model',
        
        # TODO don't combine fields in the definition and notes, fields. Use the new anki_flashcard.html 
        fields=[
            {'name': 'ID'},
            {'name': 'cloze'},
            {'name': 'hint'},
            {'name': 'definition'},
            {'name': 'notes'},
            {'name': 'image'},
            {'name': 'audio'},
        ],

        templates=[
            {
                'name': 'Card 1',
                'qfmt': qfmt_html,
                'afmt': afmt_html,
            },
        ],
        css=css_code
    )

    # Create an Anki deck
    deck_id = model_id + 1  # Ensure deck_id is different from model_id
    deck = genanki.Deck(deck_id, 'lln_anki_deck')

    # Add cards to the deck
    for index, row in df.iterrows():
        my_note = genanki.Note(
            model=model,
            fields=[(row['ID']), (row['cloze']), (row['hint']), (row['definition']), (row['notes']), (row['image']), (row['audio'])],
        )
        deck.add_note(my_note)
    
    apkg_package = genanki.Package(deck)
    # return the deck
    return apkg_package


# export the df as an anki package and csv file

@log_io
def export_df(df, package, native_language, output_file_path, encoding='utf-8'):
  """
  Exports an Anki package and a cleaned DataFrame to CSV.

  Args:
      df (pandas.DataFrame): The DataFrame to export.
      package (anki.Package): The Anki package to save.
      native_language (str): The native language of the data.
      output_file_path (str): The path to save the files.
      encoding (str, optional): The encoding for the CSV file. Defaults to 'utf-8'.

  Returns:
      tuple: A tuple containing the paths to the exported Anki package and CSV file.

  This function performs the following actions:

      1. Saves the Anki package with a timestamped filename.
      2. Replaces empty strings with NaN values in the DataFrame.
      3. Handles potential missing data by:
          - Optionally dropping columns containing only NaN values (default).
          - Optionally filling NaN values with a specified value (future implementation).
      4. Exports the cleaned DataFrame as a CSV file with a timestamped filename,
         using tab ('\t') as the delimiter and the specified encoding.

  """

  # Maintain current logic for Anki package saving
  current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
  package_path = os.path.join(output_file_path, f'{native_language}_LLN_{current_time}.apkg')
  package.write_to_file(package_path)

  # Data cleaning with flexibility
  df.replace('', np.nan, inplace=True)  # Replace empty strings with NaN (inplace modification)
  # Option 1: Drop columns with only NaN values (existing functionality)
  df.dropna(how='all', axis=1, inplace=True)

  # Option 2: Fill NaN values with a specified value (future implementation)
  # You can add logic here to fill NaN values with a desired value (e.g., df.fillna(0))

  # Save DataFrame as CSV with customizations
  csv_file_path = os.path.join(output_file_path, f'{native_language}_LLN_{current_time}.csv')
  df.to_csv(csv_file_path, index=False, sep='\t', encoding=encoding)

  return package_path, csv_file_path





    



