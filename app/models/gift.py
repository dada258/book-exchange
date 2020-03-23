#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author dage
    @Date 2020/2/27 18:54
    @Describe 
    @Version 1.0
"""
from flask import current_app
from collections import namedtuple
from app.models.base import db,Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger, desc, func
from sqlalchemy.orm import relationship
from app.models.wish import Wish


from app.spider.yushu_book import YuShuBook


class Gift(Base):
    id = Column(Integer,primary_key=True)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15),nullable=False)
    launched = Column(Boolean,default=False)


    def is_yourself_gift(self,uid):
        return True if self.uid == uid else False

    @classmethod
    def get_user_gifts(cls,uid):
        gifts = Gift.query.filter_by(uid=uid,launched=False).order_by(
            desc(Gift.create_time)).all()

        return gifts

    @classmethod
    def get_wish_counts(cls,isbn_list):

        count_list = db.session.query(func.count(Wish.id),Wish.isbn).filter(Wish.launched == False,
                                      Wish.isbn.in_(isbn_list),
                                      Wish.status == 1).group_by(
        Wish.isbn).all()

        print(count_list)

        count_list = [{'count':w[0],'isbn':w[1]} for w in count_list]

        return count_list




    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(launched=False).order_by(desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).all()




        return recent_gift

