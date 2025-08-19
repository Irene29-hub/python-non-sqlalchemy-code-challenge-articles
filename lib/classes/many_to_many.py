class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            return

class Author:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            return

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        articles = self.articles()
        return list(set([magazine.category for magazine in self.magazines()])) if articles else None

class Magazine:
    all = []
    
    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        articles = self.articles()
        return [article.title for article in articles] if articles else None

    def contributing_authors(self):
        counts = {}
        for article in self.articles():
            counts[article.author] = counts.get(article.author, 0) + 1
        result = [author for author, count in counts.items() if count > 2]
        return result if result else None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        counts = {}
        for article in Article.all:
            counts[article.magazine] = counts.get(article.magazine, 0) + 1
        return max(counts, key=counts.get)