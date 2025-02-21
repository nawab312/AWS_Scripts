import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def get_secret(secret_name):
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name='us-east-1')  # Use your region

    try:
        # Fetch the secret from Secrets Manager
        response = client.get_secret_value(SecretId=secret_name)

        # Secrets Manager returns the secret as either a string or binary data
        if 'SecretString' in response:
            secret = response['SecretString']
        else:
            secret = response['SecretBinary']

        return secret
    
    except NoCredentialsError:
        print("Credentials are not available")
    except PartialCredentialsError:
        print("Partial credentials provided")
    except Exception as e:
        print(f"Error retrieving secret: {e}")

# Example usage: Retrieve DB credentials secret
db_credentials_secret = get_secret('your-db-credentials-secret-id')

if db_credentials_secret:
    print("Secret retrieved successfully!")
    # Now you can parse and use db_credentials_secret as needed (e.g., username/password)
