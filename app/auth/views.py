from flask import render_template, session, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from app.form import LoginForm
from werkzeug.security import generate_password_hash


from . import auth
from app.firestore_service import get_user, user_put
from app.models import UserModel, UserData

@auth.route('/login', methods=['GET', 'POST']) #interpreta esto como un sitio fisico
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if login_form.validate_on_submit():

        user_name = login_form.user_name.data
        password = login_form.password.data

        user_doc = get_user(user_name)

        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']
            if password == password_from_db:
                user_data = UserData(user_name,password)
                user = UserModel(user_data)

                login_user(user)
                redirect(url_for('hello'))
            else:
                flash('la información no coincide')

        else:
            flash('el usuario no existe')    

        # flash('Nombre de usuario registrado con éxito') #los flashes hay que renderearlos en el html
        #flash eliminado porque ya no tiene sentido
        return redirect(url_for('index'))
    return render_template('login.html', **context)

@auth.route('signup', methods=['GET', 'POST'])
def singup():
    signup_form = LoginForm()
    context = {
        'signup_form': signup_form
    }
    
    if signup_form.validate_on_submit():
        user_name = signup_form.user_name.data
        password = signup_form.password.data

        user_doc = get_user(user_name)

        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(user_name, password_hash)
            user_put(user_data)

            user = UserModel(user_data)
            login_user(user)
            flash('Bienvenido')
            return redirect(url_for('hello'))

    else:
        flash('El usuario ya existe')        


    return render_template('signup.html', **context)
    pass    

@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('regresa pronto')
    return redirect(url_for('auth.login'))



    
