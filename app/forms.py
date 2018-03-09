from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    #remember_me = BooleanField('Remember Me')
    login = SubmitField('LOGIN')

class AddDishForm(FlaskForm):
	name = StringField(validators=[DataRequired()])
	items = StringField(validators=[DataRequired()])
	price = StringField(validators=[DataRequired()])
	italianbeef = StringField(validators=[DataRequired()])
	jibarito = StringField(validators=[DataRequired()])
	order = SubmitField('Add Dish')
 