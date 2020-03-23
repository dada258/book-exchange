from flask import current_app, flash, redirect, url_for, render_template

from app.ViewModel.gift import MyGifts
from app.libs.enums import PendingStatus
from app.models.base import db
from app.models.drift import Drift

from app.web.blueprint import web
from flask_login import login_required,current_user
from app.models.gift import Gift
__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    print(gifts_of_mine)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    print(isbn_list)
    wish_count_list = Gift.get_wish_counts(isbn_list)
    print(wish_count_list)
    view_model = MyGifts(gifts_of_mine,wish_count_list)
    # for i in view_model.gifts:
    #     print(i)
    #
    print(view_model.gifts)
    return render_template('my_gifts.html',gifts=view_model.gifts)
    return 'nihaoa'




@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):

        #
        # try:
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            # db.session.commit()
        # except Exception as e:
        #     db.session.rollback()

    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复提交')

    return redirect(url_for('web.book_detail',isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    gift = Gift.query.filter_by(id=gid,launched=False).first_or_404()
    drift = Drift.query.filter_by(gift_id=gid,pending=PendingStatus.Waiting).first()
    if drift:
        flash('这个礼物正处于交易状态，请先前往鱼漂完成该交易')
    else:
        with db.auto_commit():
            current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
            gift.status = 0
            gift.delete()

    return redirect(url_for('web.my_gifts'))




