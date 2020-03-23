#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author dage
    @Date 2020/3/12 20:48
    @Describe 
    @Version 1.0
"""
from .book import BookViewModel
from collections import namedtuple
MyGift = namedtuple('MyGift1111',['id','book','wishes_count'])

class MyWishes:
    def __init__(self,gifts_of_mine,wish_count_list):

        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list
        self.gifts = self.__parse()

    def __parse(self):
        tmp_gifts = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            tmp_gifts.append(my_gift)
        return tmp_gifts


    def __matching(self,gift):
        count = 0


        for wish_count in self.__wish_count_list:



            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']

        # r = {
        #
        #         'wishes_count':count,
        #         'book': BookViewModel(gift.book),
        #         'id': gift.id
        #     }
        # return r
        my_gift = MyGift(gift.id,BookViewModel(gift.book),count)
        print(my_gift)
        return my_gift

