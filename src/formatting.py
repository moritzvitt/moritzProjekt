import pandas as pd
import re
import random
from src.logging_config import log_io

@log_io
def formatting(df: pd.DataFrame):

    def create_ID(ID, source, date):
        newID = f"{ID}{source}{date}"
        newID = newID.replace(" ", "__")
        #random number
        newID = newID + "__" + str(random.randint(1000, 9999))
        return newID
    
    df["ID"] = df.apply(lambda row: create_ID(row["ID"], row["source"], row["date"]), axis=1)

    def cloze_pattern(word, phrase, synonyms):
        word_new = '{' + '{' f'c1::{word}::{synonyms}' + '}' + '}'
        # print(word_new)

        phrase = re.sub(f'{word}', word_new, phrase, flags=re.IGNORECASE)
        # print(phrase)
        return phrase
    df["cloze"] = df.apply(lambda row: cloze_pattern(row["word"], row["long_phrase"], row["synonyms"]), axis=1)

    
