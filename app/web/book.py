
from flask import jsonify,request,render_template,flash
from flask_login import current_user

from app.ViewModel.book import BookViewModel, BookCollection
from app.ViewModel.trade import TradeInfo
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key


from app.spider.yushu_book import YuShuBook

from app.web.blueprint import web
from app.models.gift import Gift
from app.models.wish import Wish
import json

# @web.route('/')
# def index1():
#     print("开始访问了")
#     return "你好啊"

@web.route('/book/search')
def search():
    """
        q : 普通关键字 isbn
        page
    """
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        #a = request.args.to_dict()
        print('访问了search页面')
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            # result = YuShuBook.search_by_isbn(q)
            # result = BookViewModel.pacage_single(result,q)
        else:
            yushu_book.search_by_keyword(q,page)
            # result = YuShuBook.search_by_keyword(q,page)
            # result = BookViewModel.package_collection(result,q)

        books.fill(yushu_book,q)
        # return jsonify(result)


        # return jsonify(books.__dict__)

    else:
        flash('搜素的关键词无效')
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    #取书籍详细数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id,isbn=isbn,launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id,isbn=isbn,launched=False).first():
            has_in_wishes =True


    trade_gifts = Gift.query.filter_by(isbn=isbn,launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn,launched=False).all()

    trade_wishes_models = TradeInfo(trade_wishes)
    trade_gifts_models = TradeInfo(trade_gifts)




    return render_template('book_detail.html',book = book,wishes=trade_wishes_models,gifts=trade_gifts_models,has_in_gifts=has_in_gifts,has_in_wishes=has_in_wishes)




@web.route('/test')
def test():
    r = {
        'name':'达达',
        'age':18
    }

    flash('hello,dada')
    flash('hello jiuyue')

    # 模板 html
    return render_template('test.html',data=r)