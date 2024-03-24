import sys
from typing import Optional
sys.path.append('../database')
from connect_db import connect_to_postgres

def add_or_update_pill(name: str, dose_size: str, pill_count: int, refill_date: Optional[str], expiry_date: Optional[str], description_of_medication: str, pills_used_per_day: int, user_id: int):
    db = connect_to_postgres()
    cursor = db.cursor()
    
    # Convert "N/A" to None for expiry_date
    expiry_date = None if expiry_date == "N/A" else expiry_date
    
    # Attempt to update first
    cursor.execute(
        'UPDATE "PrescriptionItems" SET Dosage = %s, PillCount = %s, RefillDate = %s, ExpiryDate = %s, DescriptionOfMedication = %s, PillsUsedPerDay = %s WHERE Medication = %s AND UserId = %s',
        (dose_size, get_quantity_of_pill(name, user_id) + pill_count, refill_date, expiry_date, description_of_medication, pills_used_per_day, name, user_id)
    )
    
    # If no row was updated, insert a new one
    if cursor.rowcount == 0:
        cursor.execute(
            'INSERT INTO "PrescriptionItems" (Medication, Dosage, PillCount, RefillDate, ExpiryDate, DescriptionOfMedication, PillsUsedPerDay, UserId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (name, dose_size, pill_count, refill_date, expiry_date, description_of_medication, pills_used_per_day, user_id)
        )

    db.commit()
    cursor.close()
    db.close()

def get_pills(user_id: int):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'SELECT Medication, Dosage, PillCount, RefillDate, ExpiryDate, DescriptionOfMedication, PillsUsedPerDay FROM "PrescriptionItems" WHERE UserId = %s',
        (user_id,)
    )
    pills = cursor.fetchall()
    cursor.close()
    db.close()
    return pills

def remove_pill(name: str, user_id: int):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'DELETE FROM "PrescriptionItems" WHERE Medication = %s AND UserId = %s',
        (name, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

def get_quantity_of_pill(name: str, user_id: int):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'SELECT PillCount FROM "PrescriptionItems" WHERE Medication = %s AND UserId = %s',
        (name, user_id)
    )
    quantity = cursor.fetchone()
    cursor.close()
    db.close()
    return quantity[0]