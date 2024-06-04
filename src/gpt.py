import pandas as pd
import openai
from jinja2 import Template
from typing import Dict, Union

from config import client, logger, log_io


# TODO need to adjust the df a little bit for GPT.
# TODO split the dataframe every 10 rows. insert it as string in the template
# TODO create different messages for phrase...

#Still needed to insert {{native_language}} and {{target_language}} in the template
@log_io
def create_ai_prompts(df: pd.DataFrame, merged: Dict[str, str], config: Dict[str, Union[str, bool]]) -> pd.DataFrame:

    prompts_df = pd.DataFrame()

    def replace_placeholders(config, messages):
    for key, message in merged.items():
        merged[key] = merged.format(**config)
        return merged

    # drop all unwanted fields ...

    def filter_fields(df: pd.DataFrame, wanted_fields: Dict[str, bool]) -> pd.DataFrame:
        for field, value in wanted_fields.items():
            if not value:
                df.drop(field, axis=1, inplace=True)
        return df

    # Apply filter and return the DataFrame
    prompts_df = filter_fields(prompts_df, config["wanted_fields"])
    return prompts_df



# try 3 times. If it doesn't work, just go one with the next one.

# Example of an OpenAI ChatCompletion request with stream=True and stream_options={"include_usage": True}

# a ChatCompletion request
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'user', 'content': "What's 1+1? Answer in one word."}
    ],
    temperature=0,
    stream=True,
    stream_options={"include_usage": True}, # retrieving token usage for stream response
)

for chunk in response:
    print(f"choices: {chunk.choices}\nusage: {chunk.usage}")
    print("****************")


# with streaming:     

def get_ai_response(message):
    
    # TODO create a Thread, first message: send the df and then next messages work on the df.
    # processes these several responses. 
    # maybe try sending several messages at the same time. To speed up the generation process. 
    # Especially when people want grammar explanations. 

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
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

            
    