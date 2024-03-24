import sys
sys.path.append('../database')
from connect_db import connect_to_postgres 


def add_user(user_id, password, firstname, lastname, email):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO "Users" (UserId, HashedPassword, FirstName, LastName, Email) VALUES (%s, %s, %s, %s, %s)',
        (user_id, password, firstname, lastname, email)
    )
    db.commit()
    cursor.close()
    db.close()

def get_user(user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'SELECT * FROM "Users" WHERE UserId = %s',
        (user_id)
    )
    user = cursor.fetchone()
    cursor.close()
    db.close()
    return user

def remove_user(user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'DELETE FROM "Users" WHERE UserId = %s',
        (user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def update_user_password(user_id, password):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'UPDATE "Users" SET HashedPassword = %s WHERE UserId = %s',
        (password, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def update_user_email(user_id, email):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'UPDATE "Users" SET Email = %s WHERE UserId = %s',
        (email, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def update_user_firstname(user_id, firstname):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'UPDATE "Users" SET FirstName = %s WHERE UserId = %s',
        (firstname, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def update_user_lastname(user_id, lastname):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'UPDATE "Users" SET LastName = %s WHERE UserId = %s',
        (lastname, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def get_all_users():
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'SELECT * FROM "Users"'
    )
    users = cursor.fetchall()
    cursor.close()
    db.close()
    return users
