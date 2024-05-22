import pandas as pd
from jinja2 import Template
from openai import OpenAI
import openai
import os

def create_ai_prompts(df, merged, config):

    prompts_df = pd.DataFrame()

    def load_and_resolve_template(row_dict, template_string):
        template = Template(template_string)
        resolved_template = template.render(row_dict)
        return resolved_template
    
    for message in merged:
        message_name = message
        prompts_df[message_name] = df.apply(lambda row: load_and_resolve_template(row.to_dict(), merged[message_name]), axis=1)

    print("Applied template to df; created df_messages.")

    def filter_fields(df, wanted_fields):
        for field, value in wanted_fields.items():
            if not value:
                df.drop(field, axis=1, inplace=True)
        return df

    # apply filter field to the df_messages and return the df_messages
    prompts_df = filter_fields(prompts_df, config["wanted_fields"])
    print("Filtered fields based on config.json")
    
    return prompts_df

# try 3 times. If it doesn't work, just go one with the next one.

# Configure the default for all requests:
client = OpenAI(
    # default is 2
    api_key=os.environ.get("OPENAI_API_KEY")
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
    print("\nFetchted API KEY SUCCESFULLY:  " + api_key + "\n")

    error_count = 0
    rows_to_delete = []  # List to store the indices of rows to be deleted

    for idx, row in prompts.iterrows():
        for column in prompts.columns:
            df.loc[idx, column] = func(row[column])
            if error_count >= 3:
                rows_to_delete.append(idx)  # Add the index of the current row to the listha
                break  # Exit the inner loop to move to the next row
                
    if error_count < 3:  # Check for overall success after the loop
        df = df.drop(rows_to_delete)
            # Delete the rows from the DataFrame
        return df
    
    else: # If there are more than 3 errors, return None
        df = df.drop(rows_to_delete)
        return None
            
    ##### what to do when there are more errors?