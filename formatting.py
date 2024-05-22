import pandas as pd
import re
import random
from logging_config import logger, log_io

@log_io
def formatting(df, config):

    # NOTE can potentially remove add_fields function, 
    # as the fields are passed individually to the html template 
    # instead of using definition_field

    def add_fields(df, wanted_fields):
        for field, should_add in wanted_fields.items():
            if not should_add:
                field_name = f"{field}"
                df[field_name] = ""
    add_fields(df, config["wanted_fields"])

    
    def clean_long_sentence(sentence):
        if "(" in sentence and ")" in sentence:
            cleaned_sentence = re.sub(r'\(.*?\)', '', sentence)
            return cleaned_sentence.strip()
        else:
            return sentence
        
    df["long_phrase"] = df["long_phrase"].apply(clean_long_sentence)


    def create_ID(ID, source, date):
        newID = f"{ID}{source}{date}"
        newID = newID.replace(" ", "__")
        #random number
        newID = newID + "__" + str(random.randint(1000, 9999))
        return newID
    
    df["ID"] = df.apply(lambda row: create_ID(row["ID"], row["source"], row["date"]), axis=1)


    def anki_sound_pattern(mp3):
            mp3 = "[sound:" + mp3 + "]"
            return mp3
    df["audio"] = df.apply(lambda row: anki_sound_pattern(row["audio"]), axis=1)


    def anki_image_pattern(first_jpg, second_jpg):
        image = f'<img src="{first_jpg}"><img src="{second_jpg}">'
        return image
    df["image"] = df.apply(lambda row: anki_image_pattern(row["first_jpg"], row["second_jpg"]), axis=1)


    def cloze_pattern(word, phrase, synonyms):
        word_new = '{' + '{' f'c1::{word}::{synonyms}' + '}' + '}'
        # print(word_new)

        phrase = re.sub(f'{word}', word_new, phrase, flags=re.IGNORECASE)
        # print(phrase)
        return phrase
    df["cloze"] = df.apply(lambda row: cloze_pattern(row["word"], row["long_phrase"], row["synonyms"]), axis=1)


    def clean_hint(hint):
        # print(type(hint))
        if hint != "" and ":" in hint:
            parts = re.findall(r"[:](.+)?", hint) 
            # r"[:](.+)?" worked
            return f": {parts[0]}"
        else: 
            return ""
    df["hint"] = df["hint"].apply(clean_hint)

    # TODO remove the following function, pass the fields individually to the html template  

    def definition_field(a, b, c, d, e, f):
        fields = [field for field in [a, b, c, d, e, f] if field]
        newDefinition = "<br>".join(map(str, fields))
        return newDefinition
    df["definition"] = df.apply(lambda row: definition_field(row["definition"], row["explanation"], row["grammar"], row["conjugation"], row["first_example"], row["second_example"]), axis=1)


    # TODO remove the following function, the notes field will be removed and 
    # translation, word_translation will be added individually
    def notes_field(translation, word_translation):
        translation_str = str(translation) if not pd.isnull(translation) else ""
        word_translation_str = str(word_translation) if not pd.isnull(word_translation) else ""
        newNotes = translation_str + "<br><br>" + word_translation_str + "<br>"
        return newNotes
    df["notes"] = df.apply(lambda row: notes_field(row["human_translation"], row["word_translation"]), axis=1)



