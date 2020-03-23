#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author dage
    @Date 2020/2/27 21:47
    @Describe 
    @Version 1.0
"""
from wtforms import Form,StringField,IntegerField,PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError, EqualTo

from app.models.user import User


class LoginForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64,message="邮箱必须大于8位小于64位"),Email(message="电子邮件不符合规定")])
    password = PasswordField(validators=[DataRequired(message="密码不可以为空"),Length(6,32,message="长度需满足大于6位小于32位并且同时包含大小写")])

class RegisterForm(LoginForm):
    # email = StringField(validators=[DataRequired(),Length(8,64),Email(message="电子邮件不符合规范")])
    # password = PasswordField(validators=[DataRequired(message="密码不能为空，请输入你的密码"),Length(6,32,message="长度不支持")])
    nickname = StringField(validators=[DataRequired(message="昵称不能为空"),Length(2,10)])

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self,field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class EmailForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),Email(message="电子邮件不符合规范")])


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6,32,message='密码长度至少需要在6到32个字符之间'),
        EqualTo('password2',message='两次输入的密码不相同')
    ])

    password2 = PasswordField(validators=[
        DataRequired(),
        Length(6,32)
    ])
