from Article import Article

class Author:
    _all = []

    def __init__(self, name):
        self._name = name
        self._articles = []
        self._all.append(self)

    def __str__(self):
        return self._name

    def name(self):
        return self._name

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)

    def articles(self):
        return [str(article) for article in self._articles]

    def magazines(self):
        return list(set([str(article.magazine()) for article in self._articles if article.magazine()]))

    def topic_areas(self):
        return list(set([article.magazine().category() for article in self._articles if article.magazine()]))

    @classmethod
    def all(cls):
        return cls._all
