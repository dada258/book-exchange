#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author dage
    @Date 2020/3/19 22:56
    @Describe 
    @Version 1.0
"""
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from flask_sqlalchemy import BaseQuery
from sqlalchemy import Column, Integer, SmallInteger, String

from app.libs.enums import PendingStatus
from app.models.base import Base


class Drift(Base):
    """
        具体的交易行为
    """
    id = Column(Integer,primary_key=True)


    # 邮寄信息
    recipient_name = Column(String(20),nullable=False)
    address = Column(String(100),nullable=False)
    message = Column(String(200))
    mobile = Column(String(20),nullable=False)


    # 书籍信息

    isbn = Column(String(14))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))


    # 请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))

    # 赠送者信息

    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))

    # 状态信息
    _pending = Column('pending',SmallInteger,default=1)

    @property
    def pending(self):
        return PendingStatus(self._pending)

    @pending.setter
    def pending(self,status):
        self._pending = status.value





