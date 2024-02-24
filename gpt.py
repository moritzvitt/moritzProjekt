import pandas as pd
import openai
from jinja2 import Template
import time

def create_df_messages(df, config_json):

    def load_and_resolve_template(row_dict, template_string):
        template = Template(template_string)
        resolved_template = template.render(row_dict)
        return resolved_template
    
    df_messages = pd.DataFrame()
    for message in config_json["messages"]:
        print(message)
        message_name = message
        df_messages[message_name] = df.apply(lambda row: load_and_resolve_template(row.to_dict(), config_json["messages"][message_name]), axis=1)

    def filter_fields(df_messages, wanted_fields):
        for field, value in wanted_fields.items():
            if not value:
                df_messages.drop(field, axis=1, inplace=True)
        return df_messages
    
    # apply filter field to the df_messages and return the df_messages
    df_messages = filter_fields(df_messages, config_json["wanted_fields"])
    
    return df_messages

# try 3 times. If it doesn't work, just go one with the next one.

def generate_content(message, retry_limit=3, timeout=15):
    attempt = 0
    
    while attempt < retry_limit:
        start_time = time.time()
        while True:
            try:
                if time.time() - start_time > timeout:
                    raise TimeoutError("Timeout exceeded.")
                
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": message}],
                    max_tokens=500,
                    # temperature=0.5
                )
                
                content = response.choices[0].message["content"]
                print(content)
                return content

            except TimeoutError as te:
                print(f"Attempt {attempt+1}: {te}. Retrying...")
                break  # Break out of the inner loop to increment the attempt counter
            except Exception as e:
                print(f"Attempt {attempt+1}: Encountered an error - {e}. Retrying...")
                time.sleep(1)  # Brief pause before retrying
                break  # Break out of the inner loop to increment the attempt counter
        
        attempt += 1
    
    print("Failed to generate content after multiple attempts.")
    return None

