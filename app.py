import os
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, json
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
    usernames_list = usernames[0].values()

    if request.method == "POST":
        # store a new users info
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # set error message variable
        error = None
        # Check all input fields for an input
        if not firstname or not lastname or not username or not email or not password:
            error = "Please input all fields!"
            return render_template("register.html", error=error)

        # Check for duplicate username
        for pair in usernames:
            if username == pair["username"]:
                error = "Username already exists"
                return render_template("register.html", error=error, firstname=firstname)

        # Set the regular expressions to validate email and password
        email_RegEx = "^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"
        password_RegEx = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

        # Validate Email
        if not re.match(email_RegEx, email):
            error = "Not a valid email!"
            return render_template("register.html", error=error)

        # validate password
        if not re.match(password_RegEx, password):
            error = "Password must be atleast 8 letters, with uppercase, lowercase, num and a special character. It's for your own safety!"
            return render_template("register.html", error=error)

        # Generate passwords hash
        password_hash = generate_password_hash(password)

        # Update users table with users info
        db.execute("INSERT INTO users (name, username, email, password_hash) VALUES(?,?,?,?)", firstname + " " + lastname,  username, email, password_hash)
        return redirect("/login")

    else:
        # return render_template("register.html",  usernames=usernames)
        return render_template("register.html",  usernames=json.dumps(usernames))


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
