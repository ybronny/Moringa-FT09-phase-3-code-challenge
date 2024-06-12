from .__init__ import conn, cursor
class Article:
    all = {}
    def __init__(self, title, content, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.add_to_database()
        

    def __repr__(self):
        return f'<Article {self.title}, {self.content}>'
    
    def add_to_database(self):
        sql = """
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.title, self.content, self.author_id, self.magazine_id))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            if not hasattr(self, "title"):
                self._title = title
            else:
                raise AttributeError("Cannot change the title after instantation.")
        else:
            raise ValueError("Title must be a non-empty string with characters between 5 and 50")
    
    @classmethod
    def row_to_instance(cls, row):
        article = cls.all.get(row[0])
        if article:
            article.title = row[1]
            article.content = row[2]
            article.author_id = row[3]
            article.magazine_id = row[4]
        else:
            article = cls(row[1], row[2], row[3], row[4])
            article.id = row[0]
            cls.all[article.id] = article
        
        return article