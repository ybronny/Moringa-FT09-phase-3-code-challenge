from models.author import Author
from models.magazine import Magazine
from models.article import Article

# Create instances of Author and Magazine
author1 = Author(1, 'John Doe')
magazine1 = Magazine(1, 'Tech Today', 'Technology')

# Create an Article
article1 = Article(author1, magazine1, 'The Rise of AI')

# Test Author methods
print(author1.articles())  
print(author1.magazines())  

# Test Magazine methods
print(magazine1.articles())  
print(magazine1.contributors())  
print(magazine1.article_titles())  
print(magazine1.contributing_authors())  

# Test Article methods
print(article1.get_author())  
print(article1.get_magazine())  
