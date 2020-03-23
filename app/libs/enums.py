#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author dage
    @Date 2020/3/19 23:26
    @Describe 
    @Version 1.0
"""
from enum import Enum

class PendingStatus(Enum):
    """交易转态"""
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4


    @classmethod
    def pending_str(cls,status,key):
        key_map = {

            cls.Waiting:{
                'requester':'等待对方邮寄',
                'gifter':'等待你邮寄'
            },
            cls.Reject:{
                 'requester':'对方已拒绝',
                 'gifter':'您已拒绝'
            },
            cls.Redraw:{
                 'requester':'你已撤销',
                 'gifter': '对方已撤销'
            },
            cls.Success:{
                 'requester':'对方已邮寄',
                 'gifter': '你已邮寄，交易完成'
            }
        }
        return key_map[status][key]
