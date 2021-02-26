from flask import Flask, request

app = Flask(__name__)#-----------------------esto es necesario 

@app.route('/')#-----------------------------esta es la pagina en la que inicia
def hello():
    user_ip = request.remote_addr#-----------con esto obtenemos la ip del usuario
    return f'La aplicación ahora debe funcionar, su ip es {user_ip}'


# if __name__ == "__main__":
#      app.run(port = 8080, debug = True)