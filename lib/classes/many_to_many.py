class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(title, "_title"):
            self._title = title

    # article property author
    @property
    def author(self):
        self.author
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self.author = author
    # article property magazine
    @property
    def magazine(self):
        self.magazine
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("Must be a type of magazine")
        
class Author:
    def __init__(self, name):
        self.name = name
        self.magazine = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not isinstance(name, str) and len(name) > 0 and not hasattr(self, "_name"):
            self._name = name

    def articles(self, article):
        if isinstance(article, Article):
            return [article for article in Article.all if article.author == self]

    def magazines(self, magazine):
        if isinstance(magazine, Magazine):
            return list(set([article.magazine for article in self._article]))

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self._category = category

    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0 :
            self._category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass