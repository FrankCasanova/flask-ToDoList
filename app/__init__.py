from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Confing

def create_app():
    app = Flask(__name__)#-----------------------esto es necesario 
    bootstrap = Bootstrap(app) #---------------la instancia de bootstrap recive la aplicación

    app.config.from_object(Confing) #--esto se usa como primer paso para que la ip de nuestros usuarios sean seguras

    return app


