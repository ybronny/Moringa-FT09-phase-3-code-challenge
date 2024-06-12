from .__init__ import conn, cursor
class Author:
    all = {}
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        self.add_to_database()

    def __repr__(self):
        return f'<Author {self.name}>'
    
    def add_to_database(self):
        sql = """
            INSERT INTO authors (name)
            VALUES (?)
        """
        cursor.execute(sql, (self.name,))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            if not hasattr(self, "name"):
                self._name = name
            else:
                raise AttributeError("Cannot change the name of the author after instantiation.")
        else:
            raise ValueError("Name must be a non-empty string.")
    

    @classmethod
    def row_to_instance(cls, row):
        author = cls.all.get(row[0])
        if author:
            author.name = row[1]
        else:
            author = cls(row[1], row[2], row[3], row[4])
            author.id = row[0]
            cls.all[author.id] = author
        
        return author
    
    def articles(self):
        from article import Article
        sql = """
            SELECT articles.title, articles.content FROM articles
            WHERE author_id = ?  
        """
        cursor.execute(sql, (self.id,)).fetchall()
        rows = cursor.fetchall()
        return [
            Article.row_to_instance(row) for row in rows
        ]
    
    