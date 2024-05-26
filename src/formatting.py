import pandas as pd
import re
import random
from src.logging_config import logger, log_io

@log_io
def formatting(df: pd.DataFrame):

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

    
