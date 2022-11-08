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
