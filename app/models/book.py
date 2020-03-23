#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author dage
    @Date 2020/2/17 16:00
    @Describe 
    @Version 1.0
"""
# sqlalchemy
# Flask_SQLAlchemy
from sqlalchemy import Column, Integer, String

from app.models.base import db,Base


class Book(Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False,)
    author = Column(String(30),default='未名')
    binding = Column(String(50))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15),nullable=False,unique=True)
    summary = Column(String(1000))
    iamge = Column(String(50))



    def sample(self):
        pass