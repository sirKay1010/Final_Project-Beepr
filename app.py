import os
import re

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


# Onboarding route
@app.route("/onboarding")
def index():
    """  """

    return render_template("onboarding.html")


# Register route
@app.route("/register", methods=["POST", "GET"])
def register():
    # Select all usernames
    usernames_list = []
    email_list = []
    usernames = db.execute("SELECT username, email FROM users")
    for userdata in usernames:
        usernames_list.append(userdata["username"])
        email_list.append(userdata["email"])

    if request.method == "POST":
        # store a new users info
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # set error message variable
        # error = None

        # Check all input fields for an input
        if not firstname or not lastname or not username or not email or not password:
            flash("Please input all fields!")
            return redirect("/register")
            # error = "Please input all fields!"
            # return render_template("register.html", error=error)

        # Check for duplicate username
        if username in usernames_list:
            flash("Username already exists!")
            return redirect("/register")
            # error = "Username already exists!"
            # return render_template("register.html", error=error)

        # Set the regular expressions to validate email and password
        email_RegEx = "^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"
        password_RegEx = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

        # Validate Email
        if not re.match(email_RegEx, email):
            flash("Invalid Email!")
            return redirect("/register")
            # error = "Not a valid email!"
            # return render_template("register.html", error=error)

        # Check for duplicate username
        if email in email_list:
            flash("Email already exists!")
            return redirect("/register")
            # error = "Email already exists!"
            # return render_template("register.html", error=error)

        # validate password
        if not re.match(password_RegEx, password):
            flash("Password must be atleast 8 letters, with uppercase, lowercase, num and a special character. It's for your own safety!")
            return redirect("/register")
            # error = "Password must be atleast 8 letters, with uppercase, lowercase, num and a special character. It's for your own safety!"
            # return render_template("register.html", error=error)

        # Generate passwords hash
        password_hash = generate_password_hash(password)

        # Update users table with users info
        db.execute("INSERT INTO users (name, username, email, password_hash) VALUES(?,?,?,?)", firstname + " " + lastname,  username, email, password_hash)
        return redirect("/login")

    else:
        return render_template("register.html",  usernames=usernames, usernames_list=usernames_list, email_list=email_list)


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
    #
    # Temporarily assign a session id
    session["user_id"] = 2

    """ Modify chat view function """
    if request.method == "POST":

        # Check the form that was submitted
        if request.form.get("username"):
            # Get friend data
            friend = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

            # Check if friend exists
            if not friend:
                return redirect("/chat_page")

            # Check if user is trying to self add
            if friend == db.execute("SELECT * FROM users WHERE id = ?", session["user_id"]):
                return redirect("/chat_page")

            # Insert friend into database
            db.execute("INSERT INTO friends (user_id, friends_id) VALUES (?, ?)", session["user_id"], friend[0]["id"])

            #
            return redirect("/chat_page")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        # Intialize a list to hold current user's friends
        friends = []

        # Query database for current user's friends
        friends_id = db.execute("SELECT * FROM friends WHERE user_id = ?", session["user_id"])

        # Check if user has friends
        if friends_id:
            # Query database for the usernames of the friends
            for friend_id in friends_id:
                user = db.execute("SELECT * FROM users WHERE id = ?", friend_id["friends_id"])

                # Add friend's username to the friends list
                friends.append(user[0])

        return render_template("chat_page.html", friends=friends)
