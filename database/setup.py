import sqlite3

def initialize_database():
    conn = sqlite3.connect('magazine_app.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS writers (
        id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS publications (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        genre TEXT NOT NULL
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY,
        headline TEXT NOT NULL,
        writer_id INTEGER,
        publication_id INTEGER,
        FOREIGN KEY (writer_id) REFERENCES writers(id),
        FOREIGN KEY (publication_id) REFERENCES publications(id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
