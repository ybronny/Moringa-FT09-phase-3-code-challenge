import sqlite3

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.save()

    def save(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)', (self.id, self.name, self.category))
        connection.commit()
        connection.close()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT articles.title FROM articles
        JOIN magazines ON articles.magazine_id = magazines.id
        WHERE magazines.id = ?
        ''', (self.id,))
        articles = cursor.fetchall()
        connection.close()
        return articles

    def contributors(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT DISTINCT authors.name FROM authors
        JOIN articles ON articles.author_id = authors.id
        WHERE articles.magazine_id = ?
        ''', (self.id,))
        contributors = cursor.fetchall()
        connection.close()
        return contributors

    def article_titles(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT title FROM articles WHERE magazine_id = ?
        ''', (self.id,))
        titles = cursor.fetchall()
        connection.close()
        return titles if titles else None

    def contributing_authors(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT authors.name FROM authors
        JOIN articles ON articles.author_id = authors.id
        WHERE articles.magazine_id = ?
        GROUP BY authors.name
        HAVING COUNT(articles.id) > 2
        ''', (self.id,))
        authors = cursor.fetchall()
        connection.close()
        return authors if authors else None
