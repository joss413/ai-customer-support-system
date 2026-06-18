import sqlite3
from datetime import datetime

DB_NAME = "tickets.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            complaint TEXT,
            category TEXT,
            product TEXT,
            issue_summary TEXT,
            urgency TEXT,
            sentiment TEXT,
            response TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_ticket(complaint, category, product, issue_summary, urgency, sentiment, response):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tickets (complaint, category, product, issue_summary, urgency, sentiment, response, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (complaint, category, product, issue_summary, urgency, sentiment, response, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_all_tickets():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows