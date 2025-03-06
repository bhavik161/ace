import boto3

client = boto3.client('bedrock-runtime')

def generate_sql_statement(user_input):
    """Generates an SQL statement from user input using Bedrock AI."""
    with open("prompt_redshift_3.txt", "r") as file:
        sys_prompt = file.read()
    
    response = client.converse(
        modelId='anthropic.claude-3-5-sonnet-20240620-v1:0',
        messages=[{"role": "user", "content": [{"text": user_input}]}],
        system=[{"text": sys_prompt}],
        inferenceConfig={"temperature": 1},
    )

    return response['output']['message']['content'][0]['text']
