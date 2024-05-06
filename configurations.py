import yaml

def basic_configurations(config, df):

    # need to load column_names from the config file
    target_language = config['target_language'] 
    native_language = config['native_language']

    with open('config/column_names.yaml', 'r') as file:
        data = yaml.safe_load(file)
        # the column names are stored in a list, the list's name is column_names
        column_names = data['column_names']
    
    # assign column_names to the dataframe
    df.columns = column_names

    # add columns to the dataframe
    df['native_language'] = config['native_language']
    df['target_language'] = config['target_language']

    print(f"\nnative_language: {native_language}\ntarget_language: {target_language}\ncolumn_names: {column_names}\n")

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

    return df, merged 
