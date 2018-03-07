from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    #remember_me = BooleanField('Remember Me')
    login = SubmitField('LOGIN')

#class OrderForm(FlasForm):
