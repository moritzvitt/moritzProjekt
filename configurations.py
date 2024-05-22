import yaml
from logging_config import logger, log_io

@log_io
def basic_configurations(df, target_language, native_language, column_names):
    """
    This function performs basic configurations on the input DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to be configured.
    config (dict): The configuration settings.

    Returns:
    tuple: A tuple containing the configured DataFrame and a merged object.
    """
    
    # assign column_names to the dataframe
    df.columns = column_names

    # add columns to the dataframe
    df['native_language'] = native_language
    df['target_language'] = target_language

    # Load both YAML files
    with open('config/messages.yaml', 'r') as file:
        messages_yaml = yaml.safe_load(file)

    with open('config/examples.yaml', 'r') as file:
        examples_yaml = yaml.safe_load(file)

    # Find the corresponding section in examples_yaml
    examples = examples_yaml[target_language]
    # Merge the strings from identical keys
    merged = {key: messages_yaml.get(key, '') + ' ' + examples.get(key, '') for key in set(messages_yaml) | set(examples)}
    #print every key and value in the merged dictionary
    for key, value in merged.items():
        print(key, value)

    # TODO add the possibility to submit phrases with distinct instructions?
    # drop all rows where word_or_phrase is phrase
    df = df[df['word_or_phrase'] != 'Phrase']

    return df, merged 
