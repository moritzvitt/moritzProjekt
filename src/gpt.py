import pandas as pd
from jinja2 import Template
from openai import OpenAI
import openai
import os
from logging_config import logger, log_io
from typing import Dict, Union

@log_io
def create_ai_prompts(df: pd.DataFrame, merged: Dict[str, str], config: Dict[str, Union[str, bool]]) -> pd.DataFrame:
  """
  Creates a DataFrame containing AI prompts based on a template and configuration.

  This function iterates through messages in the `merged` dictionary and applies a template
  to each row in the `df` DataFrame. The template is resolved using the `Template` class
  from the `texttemplate` library (assumed to be imported). The function then filters columns
  in the resulting DataFrame based on the `wanted_fields` key in the `config` dictionary.

  Args:
      df (pandas.DataFrame): The DataFrame containing data to be used for prompt generation.
      merged (dict[str, str]): A dictionary where keys are message names and values are template strings.
      config (dict[str, Union[str, bool]]): A configuration dictionary containing:
          * "wanted_fields": (dict[str, bool]) A dictionary where keys are column names in the
                             resulting DataFrame and values are booleans indicating inclusion (True)
                             or exclusion (False).

  Returns:
      pandas.DataFrame: A DataFrame containing the generated AI prompts.
  """

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


# try 3 times. If it doesn't work, just go one with the next one.

# Configure the default for all requests:
client = OpenAI(
    
    api_key=os.environ.get("OPENAI_API_KEY"),
    # BUG I don't use the API KEY anywhere
    # default is 2
    max_retries=0,
    timeout=30, # 10 seconds
)


def get_ai_response(message):
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": message}],
            max_tokens=500,
            model="gpt-3.5-turbo",
        )
        
        content = response.choices[0].message.content
        print(f"{content}")

        return content
    
    except openai.APITimeoutError as ate:
        print(f"{ate}. Continuing to generate the next field...")
        error_count += 1
    except Exception as e:
        print(f"Encountered an error - {e}. Continuing to generate the next field...")
        error_count += 1
    return content


# implement proper error handling with more exceptions and logging

@log_io
def handle_API_errors(func, df: pd.DataFrame, prompts: pd.DataFrame, max_retries=3) -> pd.DataFrame:
  """
  Handles potential errors during API calls for processing DataFrame rows.

  This function iterates through rows and columns in the prompts DataFrame,
  applying the provided function (func) to each cell value. It handles API errors
  by retrying the function call a limited number of times and keeping track of errors.

  Args:
      func (callable): The function to apply to each cell value.
      df (pandas.DataFrame): The DataFrame to store the processed results.
      prompts (pandas.DataFrame): The DataFrame containing the data to process.
      max_retries (int, optional): The maximum number of retries for failed API calls.
          Defaults to 3.

  Returns:
      pandas.DataFrame: The DataFrame with processed values, or None if exceeding retry limit.

  Raises:
      RuntimeError: If the API error count exceeds the retry limit for all rows.
  """

  error_count = 0
  rows_to_delete = []

  for idx, row in prompts.iterrows():
    for column in prompts.columns:
      # Apply function with error handling
      try:
        df.loc[idx, column] = func(row[column])
      except Exception as e:
        error_count += 1
        logger.error(f"Error processing row {idx}, column {column}: {e}")
        if error_count >= max_retries:
          rows_to_delete.append(idx)
          break  # Exit inner loop and move to next row

  # Handle overall success or failure
  if error_count < max_retries:
    df = df.drop(rows_to_delete)
    return df
  else:
    df = df.drop(rows_to_delete)
    raise RuntimeError(f"Exceeded maximum retries ({max_retries}) for API errors.")

            
    