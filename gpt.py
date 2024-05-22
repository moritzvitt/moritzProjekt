import pandas as pd
from jinja2 import Template
from openai import OpenAI
import openai
import os
from logging_config import logger

def create_ai_prompts(df, merged, config):

    prompts_df = pd.DataFrame()

    def load_and_resolve_template(row_dict, template_string):
        template = Template(template_string)
        resolved_template = template.render(row_dict)
        return resolved_template
    
    for message in merged:
        message_name = message
        prompts_df[message_name] = df.apply(lambda row: load_and_resolve_template(row.to_dict(), merged[message_name]), axis=1)

    def filter_fields(df, wanted_fields):
        for field, value in wanted_fields.items():
            if not value:
                df.drop(field, axis=1, inplace=True)
        return df

    # apply filter field to the df_messages and return the df_messages
    prompts_df = filter_fields(prompts_df, config["wanted_fields"])
    print("Applied template to df; created prompts_df.")
    print("Filtered fields based on config.json")
    
    return prompts_df

# try 3 times. If it doesn't work, just go one with the next one.

# TODO take following this to the config.yaml

client = OpenAI(
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


def handle_API_errors(func, df, prompts):  

    api_key = os.environ.get("OPENAI_API_KEY")

    error_count = 0
    rows_to_delete = []  # List to store the indices of rows to be deleted

    logger.info("Starting API call loop...")

    for idx, row in prompts.iterrows():
        for column in prompts.columns:
            try:
                df.loc[idx, column] = func(row[column])
            except openai.APITimeoutError as ate:
                logger.warning(f"API Timeout Error encountered for row {idx}, column {column}: {ate}")
                error_count += 1
                if error_count >= 3:
                    rows_to_delete.append(idx)
                    logger.warning(f"Maximum error threshold reached (3 errors). Stopping processing for this row.")
                    break  # Exit the inner loop to move to the next row
            except Exception as e:
                logger.error(f"Unexpected error encountered for row {idx}, column {column}: {e}")
                error_count += 1
                if error_count >= 3:
                    rows_to_delete.append(idx)
                    logger.warning(f"Maximum error threshold reached (3 errors). Stopping processing for this row.")
                    break  # Exit the inner loop to move to the next row

    if error_count < 3:  # Check for overall success after the loop
        logger.info(f"API calls completed with {error_count} errors. Cleaning DataFrame...")
        df = df.drop(rows_to_delete)
        # Delete the rows from the DataFrame
        return df
    
    else: # If there are more than 3 errors, return None
        logger.error(f"API calls failed with {error_count} errors. Maximum threshold reached. Returning None.")
        df = df.drop(rows_to_delete)
        return None

# TODO add proper error handling, exceptions and a possible retry mechanism, when it fails
# retry maybe with a command line argument like 'yes' or 'no'