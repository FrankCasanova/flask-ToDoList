from flask import Flask, request, make_response,redirect, render_template

app = Flask(__name__)#-----------------------esto es necesario 

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))#entregamos una respuesta, que redirige a la página hello
    response.set_cookie('user_ip', user_ip)#la coockie guarda la IP del usuario.

    return response #entregamos la respuesta


@app.route('/hello')#-----------------------------esta es la pagina en la que inicia
def hello():
    user_ip = request.cookies.get('user_ip') #usa la cookie con la IP del usuario mara mostrarla
    user_ip = request.remote_addr#-----------con esto obtenemos la ip del usuario
    return render_template('hello.html', user_ip=user_ip) #indicamos que queremos renderizar este template, y como parametro le damos la IP del usuario


# if __name__ == "__main__":
#      app.run(port = 8080, debug = True)