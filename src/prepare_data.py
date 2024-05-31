import pandas as pd
from jinja2 import Template
from typing import Dict, Union
from typing import List, Dict, Tuple

# dependencies from other scripts
from logging_config import log_io
from config import column_names, client

@log_io
def prepare_data(
    df: pd.DataFrame,
    target_language,
    native_language,
    messages: Dict[str, str],
    examples: Dict[str, Dict[str, str]]
) -> Tuple[pd.DataFrame, Dict[str, str]]:
    
    """
    Perform basic configurations on the input DataFrame and merge the messages and examples.

    This function sets the column names of the DataFrame, adds the native and target language columns,
    merges the messages and examples dictionaries for the target language, and removes rows where 'word_or_phrase' is 'Phrase'.

    Args:
        df: The input DataFrame to be configured.
        target_language: The target language for the examples.
        native_language: The native language to be added as a column.
        column_names: A list of column names to assign to the DataFrame.
        messages: A dictionary containing the general messages.
        examples: A dictionary containing examples, specific to the target language.

    Returns:
        A tuple containing the configured DataFrame and the merged dictionary.
    """

    # Assign column names to the DataFrame
    df.columns = column_names
    
    # If user chose different options, redefine native_language and target_language here. Standard is set in the items.csv
    df['native_language'] = native_language
    df['target_language'] = target_language

    # Extract the examples for the target language
    target_language_examples = examples.get(target_language, {})

    # Merge the messages and target language examples dictionaries
    merged = {
        key: messages.get(key, '') + ' ' + target_language_examples.get(key, '')
        for key in set(messages) | set(target_language_examples)
    }

    return df, merged


# TODO need to adjust the df a little bit for GPT.
# TODO split the dataframe every 10 rows. insert it as string in the template
# TODO create different messages for phrase...

#Still needed to insert {{native_language}} and {{target_language}} in the template
@log_io
def create_ai_prompts(df: pd.DataFrame, merged: Dict[str, str], config: Dict[str, Union[str, bool]]) -> pd.DataFrame:

  prompts_df = pd.DataFrame()

  def load_and_resolve_template(row_dict: Dict, template_string: str) -> str:
      """
      Loads and resolves a template string using the provided row dictionary.

      This is a helper function used within `create_ai_prompts`.

      Args:
          row_dict (dict): A dictionary containing data for template resolution.
          template_string (str): The template string to be resolved.

      Returns:
          str: The resolved template string.
      """
      template = Template(template_string)  # Assuming Template is from texttemplate
      resolved_template = template.render(row_dict)
      return resolved_template

  for message in merged:
      message_name = message
      prompts_df[message_name] = df.apply(lambda row: load_and_resolve_template(row.to_dict(), merged[message_name]), axis=1)

  def filter_fields(df: pd.DataFrame, wanted_fields: Dict[str, bool]) -> pd.DataFrame:
      """
      Filters columns in a DataFrame based on a dictionary of desired inclusions/exclusions.

      This is a helper function used within `create_ai_prompts`.

      Args:
          df (pandas.DataFrame): The DataFrame to be filtered.
          wanted_fields (dict[str, bool]): A dictionary where keys are column names and
                                           values are booleans indicating inclusion (True)
                                           or exclusion (False).

      Returns:
          pandas.DataFrame: The filtered DataFrame.
      """
      for field, value in wanted_fields.items():
          if not value:
              df.drop(field, axis=1, inplace=True)
      return df

  # Apply filter and return the DataFrame
  prompts_df = filter_fields(prompts_df, config["wanted_fields"])
  return prompts_df
