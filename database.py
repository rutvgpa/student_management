import sqlite3

def connect():
    return sqlite3.connect("students.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_number TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_student(roll, name, age, course):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO students (roll_number, name, age, course)
        VALUES (?, ?, ?, ?)
        """, (roll, name, age, course))

        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def search_student(roll):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll,))
    data = cursor.fetchone()

    conn.close()
    return data

def get_all_students():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    conn.close()
    return data

def delete_student(roll):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE roll_number = ?", (roll,))
    conn.commit()
    conn.close()