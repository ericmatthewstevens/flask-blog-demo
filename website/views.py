from crypt import methods
from unicodedata import category
from flask import Blueprint, render_template, request, flash
from flask_login import current_user, login_required
from .models import Post
from . import db

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
@login_required
def home():
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts) #Flask actively looks for a template. Therefore, you must specify which template for flask to use

@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')

        if not text:
            flash('Post cannot be empty', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('create_posts.html', user=current_user)