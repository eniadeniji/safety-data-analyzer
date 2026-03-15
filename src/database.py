import sqlite3

DB_PATH = "data/incidents.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            location TEXT,
            incident_type TEXT,
            severity TEXT,
            description TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_incident(date, location, incident_type, severity, description):
    conn = get_connection()
    cursor = conn.cursor()
     
    cursor.execute("""
        INSERT INTO  incidents (date, location, incident_type, severity, description)
        Values (?, ?, ?, ?, ?)
        
    """, (date, location, incident_type, severity, description))

    conn.commit()
    conn.close()
