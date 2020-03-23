#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author dage
    @Date 2020/3/11 12:29
    @Describe 
    @Version 1.0
"""
class TradeInfo:
    def __init__(self,goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self,goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]


    def __map_to_trade(self,single):
        if single.create_datetime:
            time = single.create_datetime.strftime("%Y-%m-%d")
        else:
            time = '未知'

        return dict(
                user_name = single.user.nickname,
                time = time,
                id = single.id
            )
