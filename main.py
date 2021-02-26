from flask import Flask, request, make_response,redirect, render_template

app = Flask(__name__)#-----------------------esto es necesario 

todos = ['Comprar café','Enviar solicitud de comprar','Entregar Video del producto']

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))#entregamos una respuesta, que redirige a la página hello
    response.set_cookie('user_ip', user_ip)#la coockie guarda la IP del usuario.

    return response #entregamos la respuesta


@app.route('/hello')#-----------------------------esta es la pagina en la que inicia
def hello():
    user_ip = request.cookies.get('user_ip') #usa la cookie con la IP del usuario mara mostrarla
    #user_ip = request.remote_addr#-----------con esto obtenemos la ip del usuario
  
    context={                    #este es el contexto de la aplicación, son los atributos que tomará el render_template para renderizar el template
        'user_ip' : user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)  #indicamos que queremos renderizar este template, y como parametro le damos la IP del usuario
                                                     #los 2 asteriscos expande el diccionario, muy util para renderizar el contexto sin incluir punto context.user_ip


# if __name__ == "__main__":
#      app.run(port = 8080, debug = True)