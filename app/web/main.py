from flask import render_template

from app.ViewModel.book import BookViewModel
from app.models.base import db
from app.models.gift import Gift
from app.models.user import User
from app.web.blueprint import web


__author__ = '七月'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    # user = User()
    # user.email = "123456789@qq.com"
    # user.password = "123456"
    # user.nickname = "258"
    # db.session.add(user)
    # db.session.commit()
    books = [BookViewModel(gift.book) for gift in recent_gifts]

    return render_template('index.html',recent=books)


@web.route('/personal')
def personal_center():
    pass
