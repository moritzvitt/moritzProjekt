from openai import OpenAI
import os

config = {
    "target_language": "Japanese",
    "native_language": "English",
    "wanted_fields": {
        "test": True,
        "general": False,
        "grammar": False,
        "conjugation": False,
        "word_type": False,
    },
    "model": "gpt-4o",
}

column_names = [
    "ID",
    "word_or_phrase",
    "short_phrase",
    "short_translation",
    "word",
    "stem",
    "word_type",
    "NAN",
    "word_translation",
    "website",
    "target_language",
    "native_language",
    "transliteration",
    "long_transliteration",
    "time_stamp",
    "movie_code",
    "source",
    "date",
    "long_phrase",
    "machine_translation",
    "human_translation",
    "first_jpg",
    "second_jpg",
    "audio",
]

# configuration of the anki flashcard fields
fields_config = {
    "fields": [
        {"name": "ID"},
        {"name": "cloze"},
        {"name": "hint"},
        {"name": "synonyms"},
        {"name": "explanation"},
        {"name": "grammar"},
        {"name": "conjugation"},
        {"name": "conjugation"},
        {"name": "notes"},
        {"name": "image"},
        {"name": "audio"},
    ]
}

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    max_retries=0,
    timeout=30,
    max_tokens=100000,
    model="gpt-3.5-turbo",
)
