from app import create_app
from flask import request, make_response,redirect, render_template, session
from flask.helpers import url_for 
from flask import flash
import unittest
from app.form import LoginForm
from app import create_app

app = create_app()



todos = ['Comprar café','Enviar solicitud de comprar','Entregar Video del producto']


   

@app.cli.command() #Command Line Interface. es un comando de términal
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


@app.route('/hello', methods=['GET'])#-----------------------------esta es la pagina en la que inicia
def hello():
    user_ip = session.get('user_ip') #usa la cookie con la IP del usuario mara mostrarla
    # user_ip = request.remote_addr#-----------con esto obtenemos la ip del usuario
    user_name = session.get('user_name')
    context={                    #este es el contexto de la aplicación, son los atributos que tomará el render_template para renderizar el template
        'user_ip' : user_ip,
        'todos': todos,  
        'user_name' : user_name
    }

    


    return render_template('hello.html', **context)  #indicamos que queremos renderizar este template, y como parametro le damos la IP del usuario
                                                     #los 2 asteriscos expande el diccionario, muy util para renderizar el contexto sin incluir punto context.user_ip


# if __name__ == "__main__":
#      app.run(port = 8080, debug = True)