from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db 
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
	form= NameForm()
	if form.validate_on_submit():
		#....
		return redirect(url_for('.index'))
	return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())

	page=request.args.get('page', 1, type=int)
	pagination=Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False)
	posts=pagination.items  
	return render_template('index.html', form=form, posts=posts, pagination=pagination)

@main.route('/post/<int:id>')
	def post(id):
		post = Post.query.get_or_404(id)
		return render_template('post.html', posts=[post])