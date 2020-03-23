#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author dage
    @Date 2020/3/18 15:11
    @Describe 
    @Version 1.0
"""
from app import mail
from flask_mail import Message
from flask import current_app, render_template
from threading import Thread


def send_async_email(app,msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass

def send_mail(to,subject,template,**kwargs):
    # msg = Message('测试邮件',sender='2981443146@qq.com',
    #               body='Test',recipients=['2981443146@qq.com'])

    msg = Message('[成长之路]'+ ' ' +subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template,**kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email,args=[app,msg])
    thr.start()

