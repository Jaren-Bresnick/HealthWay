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
        'UPDATE "Pharmacy" SET dose_size = %s, pill_count = pill_count + %s, refill_date = %s, expiry_date = %s, description_of_medication = %s, pills_used_per_day = %s WHERE name = %s AND user_id = %s',
        (dose_size, pill_count, refill_date, expiry_date, description_of_medication, pills_used_per_day, name, user_id)
    )
    
    # If no row was updated, insert a new one
    if cursor.rowcount == 0:
        cursor.execute(
            'INSERT INTO "Pharmacy" (name, dose_size, pill_count, refill_date, expiry_date, description_of_medication, pills_used_per_day, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (name, dose_size, pill_count, refill_date, expiry_date, description_of_medication, pills_used_per_day, user_id)
        )

    db.commit()
    cursor.close()
    db.close()

def get_pills(user_id: int):
    db = connect_to_postgres()
    cursor = db.cursor()
    cursor.execute(
        'SELECT name, dose_size, pill_count, refill_date, expiry_date, description_of_medication, pills_used_per_day FROM "Pharmacy" WHERE user_id = %s',
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
        'DELETE FROM "Pharmacy" WHERE name = %s AND user_id = %s',
        (name, user_id)
    )
    db.commit()
    cursor.close()
    db.close()

# Additional functions like updating individual pill info or removing a pill by id can be added here similarly.
