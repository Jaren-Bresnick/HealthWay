import sys
sys.path.append('../database')
from connect_db import connect_to_postgres

def add_userhealth(user_id, gender, height, weight, age, activity_level):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute('INSERT INTO "UserHealth" (UserId, Gender, UserHeight, UserWeight, UserAge, ActivityLevel) VALUES (%s, %s, %s, %s, %s, %s)',
                   user_id, gender, height, weight, age, activity_level)
    db.commit()
    cursor.close()
    db.close()

def get_userhealth(user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM "UserHealth" WHERE UserId = %s', user_id)
    userhealth = cursor.fetchone()
    cursor.close()
    db.close()
    return userhealth

def remove_userhealth(user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute('DELETE FROM "UserHealth" WHERE UserId = %s', user_id)
    db.commit()
    cursor.close()
    db.close()

def update_userhealth_gender(user_id, gender):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute('UPDATE "UserHealth" SET Gender = %s WHERE UserId = %s', gender, user_id)
    db.commit()
    cursor.close()
    db.close()

def update_userhealth_height(user_id, height):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute('UPDATE "UserHealth" SET UserHeight = %s WHERE UserId = %s', height, user_id)
    db.commit()
    cursor.close()
    db.close()

def update_userhealth_weight(user_id, weight):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute('UPDATE "UserHealth" SET UserWeight = %s WHERE UserId = %s', weight, user_id)
    db.commit()
    cursor.close()
    db.close()

def update_userhealth_age(user_id, age):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute('UPDATE "UserHealth" SET UserAge = %s WHERE UserId = %s', age, user_id)
    db.commit()
    cursor.close()
    db.close()

def update_userhealth_activity_level(user_id, activity_level):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute('UPDATE "UserHealth" SET ActivityLevel = %s WHERE UserId = %s', activity_level, user_id)
    db.commit()
    cursor.close()
    db.close()

