import pandas as pd
from jinja2 import Template


def create_df_messages(df, config_json):

    df_messages = pd.DataFrame()

    def load_and_resolve_template(row_dict, template_string):
        template = Template(template_string)
        resolved_template = template.render(row_dict)
        return resolved_template
    
    for message in config_json["messages"]:
        message_name = message
        df_messages[message_name] = df.apply(lambda row: load_and_resolve_template(row.to_dict(), config_json["messages"][message_name]), axis=1)

    print("Applied template to df; created df_messages.")

    def filter_fields(df_messages, wanted_fields):
        for field, value in wanted_fields.items():
            if not value:
                df_messages.drop(field, axis=1, inplace=True)
        return df_messages
    
    # apply filter field to the df_messages and return the df_messages
    df_messages = filter_fields(df_messages, config_json["wanted_fields"])
    print("Filtered fields based on config.json")
    
    return df_messages

# try 3 times. If it doesn't work, just go one with the next one.

from openai import OpenAI
import openai

# Configure the default for all requests:
client = OpenAI(
    # default is 2
    max_retries=0,
    timeout=30, # 10 seconds
)

def generate_content(message):
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": message}],
            max_tokens=500,
            model="gpt-4"
        )
        
        content = response.choices[0].message.content
        print(f"{content}")

        return content
    
    except openai.APITimeoutError as ate:
        print(f"{ate}. Continuing to generate the next field...")
    except Exception as e:
        print(f"Encountered an error - {e}. Continuing to generate the next field...")

    return None
