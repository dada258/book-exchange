from flask import Flask
from app.models.book import db
from flask_login import LoginManager
from flask_mail import Mail

login_manager = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    print(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint1(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "web.login"
    login_manager.login_message = "请先登录或注册"

    mail.init_app(app)

    with app.app_context():
        db.create_all()

    return app

def register_blueprint1(app):
    from app.web.blueprint import web
    app.register_blueprint(web)