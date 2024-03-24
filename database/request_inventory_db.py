import sys
sys.path.append('../database')
from connect_db import connect_to_postgres

def add_item(item_name, item_quantity, user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO "Inventory" (Product, Quantity, UserId) VALUES (%s, %s, %s)',
        (item_name, item_quantity, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def get_inventory(user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'SELECT Product, Quantity FROM "Inventory" WHERE UserId = %s',
        (user_id)
    )
    inventory = cursor.fetchall()
    cursor.close()
    db.close()
    return inventory

def remove_item(item_name, user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'DELETE FROM "Inventory" WHERE Product = %s AND UserId = %s',
        (item_name, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def remove_item_by_id(inv_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'DELETE FROM "Inventory" WHERE ID = %s',
        (inv_id)
    )
    db.commit()
    cursor.close()
    db.close()


def update_item_quantity(user_id, item_name, item_quantity):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'UPDATE "Inventory" SET Quantity = %s WHERE Product = %s AND UserId = %s',
        (item_quantity, item_name, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def update_item_quantity_by_id(id, item_quantity):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'UPDATE "Inventory" SET Quantity = %s WHERE ID = %s',
        (item_quantity, id)
    )
    db.commit()
    cursor.close()
    db.close()

def get_all_products(user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'SELECT Product FROM "Inventory" WHERE UserId = %s',
        (user_id)
    )
    products = cursor.fetchall()
    cursor.close()
    db.close()
    return products
