import genanki 
import numpy as np
import os
import time

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

def export_df (df, config, package):

    # Save the Anki package to the Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    package_path = os.path.join(desktop_path, f'{config["native_language"]}_LLN_{current_time}.apkg')
    package.write_to_file(package_path)

    print(f'Anki package "{package_path}" has been created.')

    # df = df[["synonyms", "hint", "first_example", "second_example", "explanation", "cloze", "definition", "image", "audio"]]
    
    # clean the df
    # Replace empty strings with NaN
    df = df.replace('', np.nan)
    # Drop columns that only contain NaN
    df = df.dropna(how='all', axis=1)

    # Save the DataFrame as a CSV file to the Desktop
    csv_file_path = os.path.join(desktop_path, f'{config["native_language"]}_LLN_{current_time}.csv')
    df.to_csv(csv_file_path, index=False, sep='\t')

    print(f'CSV file "{csv_file_path}" has been created.')

    return df




    



