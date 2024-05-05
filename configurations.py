import pandas as pd
import yaml

def basic_configurations(config_yaml_path, csv_file_path):

    #safe variables 'native_language' and 'target_language' 
    with open(config_yaml_path, 'r') as file:
        config_yaml = yaml.safe_load(file)
        native_language = config_yaml["native_language"]
        target_language = config_yaml["target_language"]
        column_names = config_yaml['column_names']

    # Load the csv file
    df = pd.read_csv(csv_file_path, delimiter='\t', names=column_names)

    # add columns to the dataframe
    df['native_language'] = native_language
    df['target_language'] = target_language

    print(f"\nnative_langugage: {native_language}\ntarget_language: {target_language}\ncolumn_names: {column_names}\n")

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

    # drop all rows where word_or_phrase is phrase
    df = df[df['word_or_phrase'] != 'Phrase']

    return df, config_yaml, merged 
