import pandas as pd
from jinja2 import Template
from openai import OpenAI
import openai
import os
from src.logging_config import logger, log_io
from typing import Dict, Union
from ..config.config import client



# try 3 times. If it doesn't work, just go one with the next one.


def get_ai_response(message):
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": message}],
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
      # TODO split df, append response to split part dataframe...Append split part one after another 
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

            
    