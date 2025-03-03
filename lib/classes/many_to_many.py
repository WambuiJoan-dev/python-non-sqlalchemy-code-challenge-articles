class Article:
    all = []
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self.title = title
        self._add_to_author()    # Add this article to the author's list of articles
        self._add_to_magazine()  # Add this article to the magazine's list of articles
        Article.all.append(self)
       

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
    
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if len(title) < 5 or len(title) > 50:
             raise ValueError("Title must be between 5 and 50 characters, inclusive.")

        self._title = title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,author):
        if not isinstance(author, Author):
            raise Exception("The author must be of type Author")
        self._author = author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,magazine):
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be of type Magazine")
        
        if hasattr(self, "_magazine") and self._magazine:
            self._magazine.articles().remove(self)      # Remove from old magazine

        self._magazine = magazine
        self._add_to_magazine()  # Add to new magazine

    def _add_to_author(self):
        if self._author:                  #Add this article to the author's list of articles
           self._author.articles().append(self)
    
    def _add_to_magazine(self):
        if self._magazine:
            self._magazine.articles.append(self) #Add this article to the magazine's list of articles

        
class Author:
    def __init__(self, name):
        self._name = name
        self._articles = [] #store articles written by the author

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name,str) or len(name)==0:
            raise Exception("name must be a string and length should not be zero")
        self._name = name

        if hasattr(self, "_name"):
            raise Exception("Auther's name cannot be changed")


    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if  not self._articles: #Checks if author has no articles
             return None
    
        categories = {article.magazine.category for article in self._articles}  #Set comprehension to get unique categories
        return list(categories)
        
        

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self._category = category
        self.articles = [] #Empty list _articles to store published articles.

    def article_titles(self):
        if not self._articles:
            return []
        return [article.title for article in self._articles]

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not isinstance(name,str) or len(name) <2 or len(name) >16:
            raise Exception("Name must be a string and must be between 2 and 16 characters, inclusive")
        self._name = name
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self,category):
        if not isinstance(category, str) or len(category) ==0:
            raise Exception("Category must be a string and must be longer than 0 characters")
        self._category = category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self.articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
s
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles:
            if article.author in author_counts:
                  author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1
        result = [author for author, count in author_counts.items() if count > 2] or None       
        return result if result else None           



    