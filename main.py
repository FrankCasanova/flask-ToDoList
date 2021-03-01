from app import create_app
from flask import request, make_response,redirect, render_template, session
from flask.helpers import url_for 
from flask import flash
from flask_login import login_required, current_user
import unittest
from app.form import  TodoForm, DeleteTodoForm, UpdateTodoForm
from app import create_app
from app.firestore_service import update_todo, get_todos, put_todo, delete_todo, update_todo

app = create_app()

   
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


@app.route('/hello', methods=['GET', 'POST'])#-----------------------------esta es la pagina en la que inicia
@login_required
def hello():
    user_ip = session.get('user_ip') #usa la cookie con la IP del usuario mara mostrarla
    # user_ip = request.remote_addr#-----------con esto obtenemos la ip del usuario
    user_name = current_user.id #session.get('user_name')
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()
    update_form = UpdateTodoForm()
    context={                    #este es el contexto de la aplicación, son los atributos que tomará el render_template para renderizar el template
        'user_ip' : user_ip,
        'todos': get_todos(user_id=user_name),  
        'user_name' : user_name,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_form': update_form,
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=user_name, description=todo_form.description.data)

        flash('tu tarea se creó con éxito')

        return redirect(url_for('hello'))

    return render_template('hello.html', **context)  #indicamos que queremos renderizar este template, y como parametro le damos la IP del usuario
                                                    #los 2 asteriscos expande el diccionario, muy util para renderizar el contexto sin incluir punto context.user_ip
 

@app.route('/todos/delete/<todo_id>', methods=['POST']) #generador de ruta
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)

    return redirect(url_for('hello'))

@app.route('/todos/update/<todo_id>/<int:done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id
    update_todo(user_id=user_id, todo_id=todo_id, done=done)
    
    return redirect(url_for('hello'))

    


    




# if __name__ == "__main__":
#      app.run(port = 8080, debug = True)