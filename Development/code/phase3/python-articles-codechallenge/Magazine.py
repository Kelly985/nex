
from Article import Article

class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []  
        self._all.append(self)
    
    def __str__(self):
        return self._name

    def name(self):
        return self._name

    def category(self):
        return self._category
    


    @classmethod
    def all(cls):
        return cls._all

    def contributors(self):
        return [article.author().name() for article in Article.all() if article.magazine() == self]

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls._all if magazine.name() == name), None)

    @classmethod
    def article_titles(cls):
        return [article.title() for article in Article.all() if article.magazine() == cls]

    def contributing_authors(self):
        authors = set([article.author() for article in Article.all() if article.magazine() == self])
        return [author.name() for author in authors if len(author.articles()) > 2]
