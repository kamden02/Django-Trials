from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask import Flask, render_template

app=Flask(__name__)


class NameForm(FlaskForm):
	name=StringField('enter your name', validators=[DataRequired()])
	submit=SubmitField('submit')

if __name__ == "__main__":
    app.run(debug=True)