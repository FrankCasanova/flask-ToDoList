from flask import Flask, request, make_response,redirect, render_template, session
from flask.helpers import url_for 
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired
from flask import flash
import unittest


app = Flask(__name__)#-----------------------esto es necesario 
bootstrap = Bootstrap(app) #---------------la instancia de bootstrap recive la aplicación

app.config['SECRET_KEY'] = 'SUPER SECRETO' #--esto se usa como primer paso para que la ip de nuestros usuarios sean seguras





todos = ['Comprar café','Enviar solicitud de comprar','Entregar Video del producto']


class LoginForm(FlaskForm): #esto sirve para crear formularios, en este caso, de login.
    user_name = StringField('Nombre de usuario', validators=[DataRequired()]) #importado de fields
    password = PasswordField('Password', validators=[DataRequired()]) #con validación de datos
    submit = SubmitField('Enviar') #botón para enviar los datos
   


@app.cli.command()
def test():

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


    

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)



@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))#entregamos una respuesta, que redirige a la página hello
    # response.set_cookie('user_ip', user_ip)#la coockie guarda la IP del usuario.
    session['user_ip'] = user_ip

    return response #entregamos la respuesta


@app.route('/hello', methods=['GET', 'POST'])#-----------------------------esta es la pagina en la que inicia
def hello():
    user_ip = session.get('user_ip') #usa la cookie con la IP del usuario mara mostrarla
    #user_ip = request.remote_addr#-----------con esto obtenemos la ip del usuario
    login_form = LoginForm()
    user_name = session.get('user_name')
    context={                    #este es el contexto de la aplicación, son los atributos que tomará el render_template para renderizar el template
        'user_ip' : user_ip,
        'todos': todos,
        'login_form': login_form,
        'user_name' : user_name
    }

    if login_form.validate_on_submit():
        user_name = login_form.user_name.data
        session['user_name'] = user_name

        flash('Nombre de usuario registrado con éxito') #los flashes hay que renderearlos en el html

        return redirect(url_for('index'))


    return render_template('hello.html', **context)  #indicamos que queremos renderizar este template, y como parametro le damos la IP del usuario
                                                     #los 2 asteriscos expande el diccionario, muy util para renderizar el contexto sin incluir punto context.user_ip


# if __name__ == "__main__":
#      app.run(port = 8080, debug = True)