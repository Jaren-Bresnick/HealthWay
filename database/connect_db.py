import psycopg2
# from google.cloud import secretmanager
import os
from dotenv import load_dotenv

# def get_secret(secret_id):
#     client = secretmanager.SecretManagerServiceClient()
#     name = f"projects/101299322343/secrets/{secret_id}/versions/latest"
#     response = client.access_secret_version(request={"name": name})
#     return response.payload.data.decode("UTF-8")

def connect_to_postgres():
    # Fetch PostgreSQL credentials from Secret Manager
    # postgres_username = get_secret("postgres-credentials-username")
    # postgres_password = get_secret("postgres-credentials-password")
    # postgres_host = get_secret("postgres-credentials-host")
    # postgres_db = get_secret("postgres-credentials-database")
    load_dotenv()
    postgres_db = os.environ.get('database')
    postgres_username = os.environ.get('myuser')
    postgres_password = os.environ.get('password')
    postgres_host = os.environ.get('host')
    # Establish connection to PostgreSQL
    conn = psycopg2.connect(dbname=postgres_db, user=postgres_username, password=postgres_password, host=postgres_host)

    return conn
