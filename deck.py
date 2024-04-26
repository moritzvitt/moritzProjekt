import genanki 

def generate_anki_deck(df):
    with open('anki.html', 'r', encoding='utf-8') as content_file:
        content = content_file.read()   

    # Splitting HTML content
    html_sections = content.split('<!-- html -->')

    # Assigning sections to qfmt, afmt, and css
    qfmt_html = html_sections[1]
    afmt_html = html_sections[2]
    css_code = html_sections[3]

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





















