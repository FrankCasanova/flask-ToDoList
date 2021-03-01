from flask import Blueprint


auth = Blueprint('auth', __name__, url_prefix='/auth') #todas las rutas que empiecen con /auth van a ser dirigidas a este blueprint

from . import views

