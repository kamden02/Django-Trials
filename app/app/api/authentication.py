from  .errors import unauthorized, forbidden

@auth.error_handler
def auth_error():
	return unauthorized('Invalid credentials')

@api.before_request
@auth.login_required
def before_request():
	if not g.current_user.is_anonymous and not g.current_user.confirmed:
		return forbidden('Unconfirmed account')

@api.route('/tokens/', methods=['POST'])
def get_token():
	if g.current_user.is_anonymous or g.token_used:
		return unauthorized('Invalid credentials')
	return jsonify({'token': g.current_user.generate_auth_token(expiration-3600), 'expiration': 3600})

