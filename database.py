import sqlite3


def init_db():
    conn = sqlite3.connect("memoryverse.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_type TEXT,
            title TEXT,
            description TEXT,
            file_path TEXT,
            upload_date TEXT,
            tags TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_file_record(doc_type, title, description, file_path, upload_date, tags=""):
    conn = sqlite3.connect("memoryverse.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO documents (doc_type, title, description, file_path, upload_date, tags)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (doc_type, title, description, file_path, upload_date, tags))
    conn.commit()
    doc_id = c.lastrowid
    conn.close()
    return doc_id


def get_all_records():
    conn = sqlite3.connect("memoryverse.db")
    c = conn.cursor()
    c.execute("SELECT * FROM documents ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows