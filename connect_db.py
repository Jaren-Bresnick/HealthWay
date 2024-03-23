import psycopg2
from google.cloud import secretmanager

def get_secret(secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/101299322343/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def connect_to_postgres():
    # Fetch PostgreSQL credentials from Secret Manager
    postgres_username = get_secret("postgres-credentials-username")
    postgres_password = get_secret("postgres-credentials-password")
    postgres_host = get_secret("postgres-credentials-host")
    postgres_db = get_secret("postgres-credentials-database")

    # Establish connection to PostgreSQL
    conn = psycopg2.connect(
        dbname=postgres_db,
        user=postgres_username,
        password=postgres_password,
        host=postgres_host
    )

    return conn

def main():
    try:
        # Connect to PostgreSQL
        conn = connect_to_postgres()
        print("Connected to PostgreSQL successfully!")

        # Perform database operations
        # For example:
        # cursor = conn.cursor()
        # cursor.execute("SELECT * FROM your_table")
        # rows = cursor.fetchall()
        # print(rows)

        # Don't forget to close the connection when done
        conn.close()
        print("Connection to PostgreSQL closed.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
