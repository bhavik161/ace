import boto3
import json
from botocore.exceptions import ClientError

def get_secret():
    """Retrieves Redshift credentials from AWS Secrets Manager."""
    secret_name = "<secret-name>"
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        response = client.get_secret_value(SecretId=secret_name)
        return json.loads(response['SecretString'])
    except ClientError as e:
        print(f"Error retrieving secret: {e}")
        return None
