from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
def home():
    return render_template("home.html", name="Flask") #Flask actively looks for a template. Therefore, you must specify which template for flask to use
