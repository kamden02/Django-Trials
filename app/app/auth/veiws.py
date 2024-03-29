from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, current_user
from . import auth
from  ..models import User  
from .forms import LoginForm
from ..email import send_email

@auth.route('login', methods=['GET', 'POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			next=request.args.get('next')
			if next is None or not next.startswith('/'):
				next= url_for('main.index')
			return redirect(next)
		flash('invalid username or password')
	reurn render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('you have been logout successfully')
	return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
	form=RegistrationForm()
	if form.validate_on_submit():
		user=User(email=form.email.data, username=form.username.data, password=form.password.data)
		db.session.add(user)
		db.session.commit()
		token=user.generate_confirmation_token()
		send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user=user, token=token)
		flash('A confirmation email has been sent to you by email')
		return redirect(url_for('main.index'))
	return render_template('auth/register.html', form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
	if current_user.confirmed:
		return redirect(url_for('main.index'))
	if current_user.confirmed(token):
		db.session.commit()
		flash('You have confirmed your Account. Thanks!')
	else:
		flash('The confirmation link is invalid or has expired')
	return redirect(url_for('main.index'))

@auth.before_app_request
def before_request():
	if current_user.is_authenticated
	 	current_user.ping()
	 	if not current_user.confirmed and request.blueprint != 'auth' and request.endpoint != 'static':
			return redirect(url_for('auth.unconfirmed'))


@app.route('/unconfirmed')
def unconfimed():
	if current_user.is_anonymous or current_user.confirmed:
		return redirect(url_for('main.index'))
	return render_template('auth/unconfirmed.html')

@app.route('/confirm')
@login_required
def resend_confimation():
	token=current_user.generate_confirmation_token()
	send_email(current_user.email, 'Confirm Your Account', 'auth/email/confirm', user=current_user, token=token)
	flash('A new confirmation email has been sent to your mail')
	return redirect(url_for('main.index'))

@main.route('/user/<username>')
def user(username):
	user=User.query.filter_by(username=username).first_or_404()
	return render_template('user.html', user=user)

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form=EditProfileForm()
	if form.validate_on_submit():
		current_user.name=form.name.data  
		current_user.location=form.location.data
		current_user.about_me=form.about_me.data  
		db.session.add(current_user._get_current_object())
		db.session.commit()
		flash('Your profile has been updated')
		return redirect(url_for('.user', username=current_user.username))
	form.name.data=current_user.name  
	form.location.data=current_user.location
	form.about_me.data=about_me
	return render_template('edit_profile.html', form=form)