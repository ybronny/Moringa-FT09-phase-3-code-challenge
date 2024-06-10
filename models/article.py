import sqlite3

class Article:
    def __init__(self, id, title, author_id, magazine_id):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.save()

    def save(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO articles (id, title, author_id, magazine_id)
        VALUES (?, ?, ?, ?)
        ''', (self.id, self.title, self.author_id, self.magazine_id))
        connection.commit()
        connection.close()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    def get_author(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT authors.name FROM authors
        JOIN articles ON articles.author_id = authors.id
        WHERE articles.id = ?
        ''', (self.id,))
        author = cursor.fetchone()
        connection.close()
        return author

    def get_magazine(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT magazines.name FROM magazines
        JOIN articles ON articles.magazine_id = magazines.id
        WHERE articles.id = ?
        ''', (self.id,))
        magazine = cursor.fetchone()
        connection.close()
        return magazine
