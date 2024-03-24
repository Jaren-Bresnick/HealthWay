import sys
sys.path.append('../database')
from connect_db import connect_to_postgres

def add_pharmacy_item(product, dosage, quantity, refills, expiration_date, user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO "Pharmacy" (Product, Dosage, Quantity, Refills, ExpirationDate, UserId) VALUES (%s, %s, %s, %s, %s, %s)',
        (product, dosage, quantity, refills, expiration_date, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def get_pharmacy_items(user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'SELECT Product, Dosage, Quantity, Refills, ExpirationDate FROM "Pharmacy" WHERE UserId = %s',
        (user_id,)
    )
    items = cursor.fetchall()
    cursor.close()
    db.close()
    return items

def remove_pharmacy_item(product, user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'DELETE FROM "Pharmacy" WHERE Product = %s AND UserId = %s',
        (product, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def update_pharmacy_item(user_id, product, dosage, quantity, refills, expiration_date):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'UPDATE "Pharmacy" SET Dosage = %s, Quantity = %s, Refills = %s, ExpirationDate = %s WHERE Product = %s AND UserId = %s',
        (dosage, quantity, refills, expiration_date, product, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def get_pharmacy_product_by_name(user_id, product_name):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'SELECT Product, Dosage, Quantity, Refills, ExpirationDate FROM "Pharmacy" WHERE Product = %s AND UserId = %s',
        (product_name, user_id)
    )
    product = cursor.fetchone()
    cursor.close()
    db.close()
    return product

# Feel free to add more functions as necessary for your application's needs.
