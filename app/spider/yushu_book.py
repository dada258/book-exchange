from app.libs.http1 import HTTP
from flask import current_app

class YuShuBook:
    isbn_url = 'https://api.douban.com/v2/book/isbn/{}?apikey=0b2bdeda43b5688921839c8ecb20399b'
    keyworda_url = 'https://api.douban.com/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self,isbn):
        url = self.isbn_url.format(isbn)
        print(url)
        result = HTTP.get(url)

        self.__fill_single(result)

    def search_by_keyword(self,keyword,page=1):
        url = self.keyworda_url.format(keyword,current_app.config['PER_PAGE'],self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def __fill_single(self,data):
        if data:
            self.total = 1
            self.books.append(data)


    def __fill_collection(self,data):

        self.total = data['total']
        self.books = data['books']


    def calculate_start(self,page):
        the_counts = (page - 1) * current_app.config['PER_PAGE']
        return the_counts

    @property
    def first(self):
        return self.books[0] if self.total >=1 else None