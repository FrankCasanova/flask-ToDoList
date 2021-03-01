from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired




class LoginForm(FlaskForm): #esto sirve para crear formularios, en este caso, de login.
    user_name = StringField('Nombre de usuario', validators=[DataRequired()]) #importado de fields
    password = PasswordField('Password', validators=[DataRequired()]) #con validación de datos
    submit = SubmitField('Enviar') #botón para enviar los datos


class TodoForm(FlaskForm):

    description = StringField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Crear')

class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Borrar')
