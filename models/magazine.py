from .__init__ import conn, cursor
class Magazine:
    all = {}
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category
        self.add_to_database()

    def __repr__(self):
        return f'<Magazine {self.name}>'
    
    def add_to_database(self):
        sql = """
            INSERT INTO magazines (name, category)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.name, self.category))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string with the number of characters between 2 and 16.")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")
        
    @classmethod
    def row_to_instance(cls, row):
        magazine = cls.all.get(row[0])
        if magazine:
            magazine.name = row[1]
            magazine.category = row[2]
        else:
            magazine = cls(row[1], row[2])
            magazine.id = row[0]
            cls.all[magazine.id] = magazine
        
        return magazine