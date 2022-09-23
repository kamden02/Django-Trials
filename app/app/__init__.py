from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view= 'auth.login'


def create_app(config_name):

	from .api import api as api_blueprint
	app.register_blueprint(api_blueprint, url_prefix='/api/v1')
	
	login_manager.init_app(app)
	
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')

	return app