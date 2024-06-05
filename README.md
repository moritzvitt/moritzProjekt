# Automatic Flashcard creation (Anki) with chatGPT

```python
if value in items:
	print(value)
```

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

```mermaid
flowchart TD
    A[Start] --> B[Load Configuration Files]
    B --> C[Load DataFrame]
    C --> D[Main Function]

    subgraph Main Function
        D --> E[Load column_names.yaml]:::file
        D --> F[Load messages.yaml]:::file
        D --> G[Load examples.yaml]:::file
        D --> H[Basic Configurations]
        H --> I[Create AI Prompts]
        I --> J[Handle API Errors]
        J --> K[Format DataFrame]
        K --> L[Add Furigana]
        L --> M[Generate Anki Deck]:::file
        M --> N[Return package and DataFrame]
    end

    N --> O[Export DataFrame]

    subgraph Export DataFrame
        O --> P[Export Anki Package]
        O --> Q[Clean DataFrame]
        Q --> R[Export CSV]
    end

    P --> S[Output: Anki Package]
    R --> T[Output: CSV File]

    A --> U[Input: config.yaml]:::file
    A --> V[Input: test_dataframes/jn_items.csv]:::file

    C --> U
    C --> V

  
    click U "config/config.yaml"
    click V "test_dataframes/jn_items.csv"
    click E "config/column_names.yaml"
    click F "config/messages.yaml"
    click G "config/examples.yaml"
    click M "deck.py"
    click O "deck.py"

```
