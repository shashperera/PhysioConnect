from db_connection import get_db_connection

# List of new exercises to be added
new_exercises = [
    {"name": "Shoulder Rolls", "description": "Lift your shoulders towards your ears and roll them backwards."},
    {"name": "Triceps Stretch", "description": "Reach one arm overhead and bend the elbow to stretch the triceps."},
    {"name": "Neck Tilt", "description": "Gently tilt your head towards your shoulder to stretch the neck."},
    {"name": "Seated Spinal Twist", "description": "Sit and twist your torso gently to stretch the spine."},
    {"name": "Wrist Flexor Stretch", "description": "Extend one arm with the palm up and gently pull back on the fingers."},
    {"name": "Ankle Circles", "description": "Rotate your ankles in circles to improve mobility."},
]

def add_exercises():
    conn = get_db_connection()
    cursor = conn.cursor()
    for ex in new_exercises:
        cursor.execute(
            "INSERT INTO exercises (name, description) VALUES (?, ?)",
            (ex["name"], ex["description"])
        )
    conn.commit()
    print(f"Added {len(new_exercises)} new exercises to the database.")
    conn.close()

if __name__ == "__main__":
    add_exercises()