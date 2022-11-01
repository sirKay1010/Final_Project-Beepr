import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

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


# Onboarding route
@app.route("/onboarding")
def index():
    """  """

    return render_template("onboarding.html")


# Register route
@app.route("/register", methods=["POST", "GET"])
def register():
    # Select all usernames
    usernames = db.execute("SELECT username FROM users")
    if request.method == "POST":
        # create a dictionary to store a new users info
        new_users = {}
        new_users["firstname"] = request.form.get("firstname")
        new_users["lastname"] = request.form.get("lastname")
        new_users["username"] = request.form.get("username")
        new_users["email"] = request.form.get("email")
        new_users["password"] = request.form.get("password")

        # What happens if code enters this if block? @mrsinister and @palmwinecode.
        if not new_users["firstname"] or not new_users["lastname"] or not new_users["username"] or not new_users["email"] or not new_users["password"]:
            return redirect("/register")

        # Check for duplicate username
        for pair in usernames:
            if new_users["username"] == pair["username"]:
                # What happens if username already exists @mrsinister and @palmwinecode.
                return redirect("/register")

        password_hash = generate_password_hash(new_users["password"])
        db.execute("INSERT INTO users (name, username, email, password_hash) VALUES(?,?,?,?)", new_users["firstname"] + " " + new_users["lastname"],  new_users["username"], new_users["email"], password_hash)
        return redirect("/login")

    # if method is GET
    else:
        return render_template("register.html")


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass
    else:
        return render_template("login.html")


# Logout route
@app.route("/logout")
def logout():
    """ Write Logout view function """


# chat_page route
@app.route("/chat_page", methods=["GET", "POST"])
def chat():
    """ Modify chat view function """
    if request.method == "POST":
        pass
    else:
        return render_template("chat_page.html")
