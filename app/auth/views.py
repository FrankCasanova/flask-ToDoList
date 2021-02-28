from flask import render_template, session, redirect, url_for, flash
from app.form import LoginForm
from . import auth

@auth.route('/login', methods=['GET', 'POST']) #interpreta esto como un sitio fisico
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if login_form.validate_on_submit():
        user_name = login_form.user_name.data
        session['user_name'] = user_name

        flash('Nombre de usuario registrado con éxito') #los flashes hay que renderearlos en el html

        return redirect(url_for('index'))
    return render_template('login.html', **context)
    