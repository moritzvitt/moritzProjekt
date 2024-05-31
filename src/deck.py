import genanki
import numpy as np
import pandas as pd
import os
import time
from src.logging_config import logger, log_io
from typing import Tuple

from config import fields_config

with open('templates/anki_card.html', 'r', encoding='utf-8') as content_file:
        content = content_file.read()

@log_io
def generate_anki_deck(df: pd.DataFrame, card_layout) -> genanki.Package:
    """Generates an Anki deck from a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing card data.

    Returns:
        genanki.Package: The generated Anki package.
    """
    
    with open('templates/anki_card.html', 'r', encoding='utf-8') as content_file:
        content = content_file.read()

    # Splitting HTML content
    html_sections = content.split('<!-- html -->')

    # Assigning sections to qfmt, afmt, and css
    qfmt_html = html_sections[1]
    afmt_html = html_sections[2]

    with open('static/css/anki_card.css', 'r', encoding='utf-8') as content_file:
        css_code = content_file.read()

    # Ensure all columns are strings
    df = df.astype(str)

    # Define the Anki model
    model_id = 1607392319
    model = genanki.Model(
        model_id,
        'Language Learning with Netflix Model',
        fields = fields_config["fields"],
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
            fields=[row['ID'], row['cloze'], row['hint'], row['definition'], row['notes'], row['image'], row['audio']],
        )
        deck.add_note(my_note)

    apkg_package = genanki.Package(deck)
    return apkg_package

@log_io
def export_df(df: pd.DataFrame, package: genanki.Package, native_language: str, output_file_path: str, encoding: str = 'utf-8') -> Tuple[str, str]:
    """Exports an Anki package and a cleaned DataFrame to CSV.

    Args:
        df (pd.DataFrame): The DataFrame to export.
        package (genanki.Package): The Anki package to save.
        native_language (str): The native language of the data.
        output_file_path (str): The path to save the files.
        encoding (str, optional): The encoding for the CSV file. Defaults to 'utf-8'.

    Returns:
        Tuple[str, str]: A tuple containing the paths to the exported Anki package and CSV file.
    """
    current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    package_path = os.path.join(output_file_path, f'{native_language}_LLN_{current_time}.apkg')
    package.write_to_file(package_path)

    csv_file_path = os.path.join(output_file_path, f'{native_language}_LLN_{current_time}.csv')
    df.to_csv(csv_file_path, index=False, sep='\t', encoding=encoding)

    return package_path, csv_file_path
