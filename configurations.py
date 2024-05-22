import yaml
from logging_config import log_io

@log_io
def basic_configurations(df, target_language, native_language, column_names, messages, examples):
    """
    This function performs basic configurations on the input DataFrame and merges the messages and examples dictionaries.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to be configured.
    config (dict): The configuration settings.
    column_names (list): A list of column names.
    messages (dict): A dictionary containing the general messages.
    examples (dict): A dictionary containing examples, specific to the target language.

    Returns:
    tuple: A tuple containing the configured DataFrame and a merged dictionary.
    """
    
    # assign column_names to the dataframe
    df.columns = column_names
    
    # add columns to the dataframe
    df['native_language'] = native_language
    df['target_language'] = target_language

    # Find the corresponding section in examples_yaml
    examples = examples[target_language]
    # Merge the strings from identical keys
    merged = {key: messages.get(key, '') + ' ' + examples.get(key, '') for key in set(messages) | set(examples)}

    # TODO add the possibility to submit phrases with distinct instructions? (maybe using python classes)
    # drop all rows where word_or_phrase is phrase
    df = df[df['word_or_phrase'] != 'Phrase']

    return df, merged 

