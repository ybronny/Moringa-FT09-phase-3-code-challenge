import sqlite3

class riter:
    def __init__(self, identifier, full_name):
        self.identifier = identifier
        self.full_name = full_name
        self.persist()

    def persist(self):
        conn = sqlite3.connect('magazine_app.db')
        c = conn.cursor()
        c.execute('INSERT INTO writers (id, full_name) VALUES (?, ?)', (self.identifier, self.full_name))
        conn.commit()
        conn.close()

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        if not isinstance(value, int):
            raise ValueError("Identifier must be an integer")
        self._identifier = value

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Full name must be a non-empty string")
        self._full_name = value

    def written_articles(self):
        conn = sqlite3.connect('magazine_app.db')
        c = conn.cursor()
        c.execute('''
        SELECT entries.headline FROM entries
        JOIN writers ON entries.writer_id = writers.id
        WHERE writers.id = ?
        ''', (self.identifier,))
        articles = c.fetchall()
        conn.close()
        return articles

    def associated_publications(self):
        conn = sqlite3.connect('magazine_app.db')
        c = conn.cursor()
        c.execute('''
        SELECT DISTINCT publications.title FROM publications
        JOIN entries ON entries.publication_id = publications.id
        WHERE entries.writer_id = ?
        ''', (self.identifier,))
        publications = c.fetchall()
        conn.close()
        return publications
