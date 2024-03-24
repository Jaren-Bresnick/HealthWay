import psycopg2
# from google.cloud import secretmanager
import os
from dotenv import load_dotenv


def connect_to_postgres():
    load_dotenv()
    postgres_db = os.environ.get('database')
    postgres_username = os.environ.get('myuser')
    postgres_password = os.environ.get('password')
    postgres_host = os.environ.get('host')
    # Establish connection to PostgreSQL
    conn = psycopg2.connect(dbname=postgres_db, user=postgres_username, password=postgres_password, host=postgres_host)

    return conn

def main(): 
    conn = connect_to_postgres()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE "Pills";')
    # cursor.execute('CREATE TABLE "Users" (UserId VARCHAR(50) PRIMARY KEY, HashedPassword VARCHAR(100), FirstName VARCHAR(50), LastName VARCHAR(50), Email VARCHAR(50));')
    # cursor.execute('CREATE TABLE "Inventory" (ID SERIAL PRIMARY KEY, UserId VARCHAR(50), Product VARCHAR(100), Quantity INT, CONSTRAINT fk_constraint FOREIGN KEY (UserId) REFERENCES "Users"(UserId) ON DELETE CASCADE);')
    # cursor.execute('CREATE TABLE "UserHealth" (UserId VARCHAR(50), Gender VARCHAR(25), UserHeight INT, UserWeight INT, UserAge INT, ActivityLevel VARCHAR(100), CONSTRAINT fk_constraint FOREIGN KEY (UserId) REFERENCES "Users"(UserId) ON DELETE CASCADE);')
    # cursor.execute('CREATE TABLE "Pills" (UserId VARCHAR(50), PillName VARCHAR(100), PillDosage VARCHAR(100), PillQuantity INT, RefillDate DATE, ExpirationDate DATE, CONSTRAINT fk_constraint FOREIGN KEY (UserId) REFERENCES "Users"(UserId) ON DELETE CASCADE);')
    cursor.execute('CREATE TABLE "PrescriptionItems" (Medication VARCHAR(100), Dosage VARCHAR(100), PillCount INT, RefillDate DATE, ExpiryDate DATE, PillsUsedPerDay INT, UserId VARCHAR(50), CONSTRAINT fk_constraint FOREIGN KEY (UserId) REFERENCES "Users"(UserId) ON DELETE CASCADE);')
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
