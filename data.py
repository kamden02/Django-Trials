import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir=os.path.abspath(os.path.dirname('/home/cipher/Desktop/project flask/'))
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL']= 'sqlite:///'+ os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class User(db.Model):
	__tablename__='users'
	id=db.column(db.Integer, primary_key=True)
	username=db.column(db.String(64))

	def __repr__(self):
		return '<User %r' %self.username