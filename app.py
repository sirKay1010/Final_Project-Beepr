import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///beepr.db")

# request handling
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# ... route
@app.route("/onboarding")
def index():
    """  """

    return render_template("onboarding.html")


# Register route
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        pass
    # if method is GET
    else:
        return render_template("register.html")


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():

    # forget any existing user alredy logged in
    session.clear()

    # error for error messages and specific html element id
    error = None
    element_id = None

    # if login form was submitted
    if request.method == "POST":


        # if no username was typed
        if not request.form.get("username"):
            error = "Please enter a username"
            element_id = "#floatingUsername"
            return render_template("login.html", error=error, element_id=element_id)

        # if no password was entered
        if not request.form.get("password"):
            error = "Please type in your password"
            element_id = "#floatingPassword"
            return render_template("login.html", error=error, element_id=element_id)

        # get the user info from the name
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        print(rows)

        # if username does not exist
        if not rows:
            error = "This username does not exist"
            element_id = "#floatingUsername"
            return render_template("login.html", error=error, element_id=element_id)

        # if username exists but password is wrong
        if not check_password_hash(rows[0]["password_hash"], request.form.get("password")):
            error = "Incorrect Password"
            element_id = "#floatingPassword"
            return render_template("login.html", error=error, element_id=element_id)

        # if remember me was selected
        if request.form.get("remember_me"):
            session.permanent = True


        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/chat_page")

    # if method used was GET
    else:
        return render_template("login.html")


# Logout route
@app.route("/logout")
def logout():
    """ Write Logout view function """


# chat_page route
@app.route("/chat_page", methods=["GET", "POST"])
@login_required
def chat():
    """ Modify chat view function """
    if request.method == "POST":
        pass
    else:
        return render_template("chat_page.html")