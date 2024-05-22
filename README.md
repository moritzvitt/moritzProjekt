# Automatic Flashcard creation (Anki) with chatGPT

A web interface, that allows you to transform the export.csv from LanguageReactor into beautiful, custom flashcards for the SRS Program ANKI. 
Just choose your dataframe, which fields you would like to generate and it will return an .apkg as well as a .csv file.

```mermaid
  graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D;
```

```mermaid
graph LR;
    A[Choose data and config] --> B{Load data CSV};
    B --> C{Load config YAML};
    C --> D{Basic configurations};
    D --> E{Create AI prompts};
    E --> F{Handle API errors};
    F --> R(get_API_response)
    F --> G{Formatting};
    G --> H{Add Furigana};
    H --> I{Generate Anki deck};
    I --> J{Export data CSV & Anki package};
```



