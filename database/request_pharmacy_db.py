import sys
sys.path.append('../database')
from connect_db import connect_to_postgres

def add_pharmacy_item(product, dosage, quantity, refills, expiration_date, pills_per_day, description_of_medication, user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO "PrescriptionItems" (Medication, Dosage, PillCount, RefillDate, ExpiryDate, PillsUsedPerDay, DescriptionOfMedication, UserId) VALUES (%s, %s, %s, %s, %s, %s)',
        (product, dosage, quantity, refills, expiration_date, pills_per_day, description_of_medication, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def get_pharmacy_items(user_id):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'SELECT Medication, Dosage, PillCount, RefillDate, ExpiryDate, PillsUsedPerDay, DescriptionOfMedication FROM "PrescriptionItems" WHERE UserId = %s',
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
        'DELETE FROM "PrescriptionItems" WHERE Medication = %s AND UserId = %s',
        (product, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def update_pharmacy_item(user_id, product, dosage, quantity, refills, expiration_date, pills_per_day, description_of_medication):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'UPDATE "PrescriptionItems" SET Dosage = %s, PillCount = %s, RefillDate = %s, ExpiryDate = %s, PillsUsedPerDay = %s, DescriptionOfMedication = %s, WHERE Medication = %s AND UserId = %s',
        (dosage, quantity, refills, expiration_date, pills_per_day, description_of_medication, product, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def get_pharmacy_product_by_name(user_id, product_name):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'SELECT Medication, Dosage, PillCount, RefillDate, ExpiryDate, PillsUsedPerDay, DescriptionOfMedication FROM "PrescriptionItems" WHERE Product = %s AND UserId = %s',
        (product_name, user_id)
    )
    product = cursor.fetchone()
    cursor.close()
    db.close()
    return product

