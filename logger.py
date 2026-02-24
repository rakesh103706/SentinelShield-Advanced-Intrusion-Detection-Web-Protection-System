import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            attack TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_event(ip, attack):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO logs (ip, attack, timestamp) VALUES (?, ?, ?)",
              (ip, attack, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()