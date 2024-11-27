import sqlite3
import json

def init_db():
    conn = sqlite3.connect("sessions.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY,
            admins TEXT,
            participants TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_session(session_id, admins, participants):
    conn = sqlite3.connect("sessions.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sessions (id, admins, participants)
        VALUES (?, ?, ?)
    """, (session_id, json.dumps(admins), json.dumps(participants)))
    conn.commit()
    conn.close()

def get_session(session_id):
    conn = sqlite3.connect("sessions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT admins, participants FROM sessions WHERE id = ?", (session_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"admins": json.loads(row[0]), "participants": json.loads(row[1])}
    return None
