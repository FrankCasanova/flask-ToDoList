from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from .config import Confing
from .auth import auth
from .models import UserModel

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_name):
    return UserModel.query(user_name)


def create_app():
    app = Flask(__name__)#-----------------------esto es necesario 
    bootstrap = Bootstrap(app) #---------------la instancia de bootstrap recive la aplicación

    app.config.from_object(Confing) #--esto se usa como primer paso para que la ip de nuestros usuarios sean seguras

    login_manager.init_app(app)

    app.register_blueprint(auth)


    return app


