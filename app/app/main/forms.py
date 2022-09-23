from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
	email=StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
	password=PasswordField('Password', validators=[DataRequired()])
	remember_me=BooleanField('keep me logged in')
	submit=SubmitField('login')

 
class RegistrationForm(FlaskForm):
	email=StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
	username=StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]$', 0, 'Usernames must have only letters, numbers, dots or underscores')])
	password=PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='passwords must match.')])
	password2=PasswordField('confirm password', validators=[DataRequired()])
	sumit=SubmitField('Register')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered')

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username aleady in use')

class EditProfileForm(FlaskForm):
	name=StringField('Real name', validators=[Length(0, 64)])
	location=StringField('Location', validators=[Length(0, 64)])
	about_me=TextAeaField('about me')
	submit=SubmitField('submit')
