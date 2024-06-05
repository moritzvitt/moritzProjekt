# LanguageReactor2Anki

A library of prompts, that allows to easily process the export items.csv from the google extension 'LanguageReactor' using AI.


1. Select the prompt for the language you are learning: 
   1. there is a _general_prompt.md and an __examples.md for each language. 
      - Japanese also contains a prompt to add furigana to each word. 

2. From your 'items.csv' select the columns 'Word', 'Context' and 'Context machine translation' and send them together with the prompt to chatGPT.
3. You will obtain a table, that should contain 7 columns with following column names:
   - 'Word'
   - 'Context'
   - 'Synonyms'
   - 'Translations'
   - 'Example'
   - 'Example translation'
   - 'Explanation'

   1. check, if everything is as you wish. 
   2. Check the header (the column names) of the table. They need to be exactly like the column names specified above.

4. asks chatGPT to provide the table as .csv
5. Check if 