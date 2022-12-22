#### Video Demo:  <URL HERE>

#### Description:
This Repository contains all files involved in the development of Beepr, which includes the Static, templates and flask_session folders, app.py (python application file) and beepr.db (a database file). BeepR is a simple, userfriendly chat app developed as a final project for Havards CS50x course in 2022.

Beepr is an web app which is built using the python flask framework. The application file(app.py) contains the logic for the backend of the website. Specifically the database accessing, registration and login authentication.

The static file contains the javascript and CSS files that allow for the responsiveness, styling and interactivity of the web app.

In order to implement the live chatting functionality we made use of socket programming; specifically the flask-SocketIO library. The app.py file contains several functions which were used as event buckets for the sending, receiving and inserting of messages into the database. Other features that required realtime two way communication such as looking up friends profiles, leaving and joining rooms were also implemented using socketIO

The styles.css file contains the css for the app.\
The script.js file contains the javascript for the app.\
The script.js handles the functionality of sending messages to the backend, and recieving them, adding new users, viewing friends profiles, starting a chat, all through socket programming

The template folder contains all the template files for the webapp. These include the default page when you enter the app which offers a little description about what the app is about and links which lead you to either the login page if you have an account or the register page if you are a newcomer.


Layout.html is a html file which contains the general html template of the entire app. it includes all the js files, css and the script tags for the socketIO. All other html files extend from this file


The register page is a html page with a form that asks for your first and last names, username, password and email.\
This page is handled by the register function in the app.py

```
The username must be unique
The password must be above 8 characters, must include an uppercase character, a special character and a number. To achieve this, a password regex is used the app.py file.
An email regex is also used to check the validity of email to make sure any email inserted matches standard email address patterns.
```


The login.html page is handled by the the login function in the app.py file.\
login.html has two fields which must be filled before the form can be submitted.\
Incorrect parameters will be flagged by the login function and the error will be displayed with red text on the page


The chatpage.html contains the meat of the app. It contains two main sections:
```
The right section which contains the chat area in which the current chat is displayed, and messages are sent and received in real time
The left section in which the user's profile, the logout button and the user's existing chats are displayed.
Hovering over the left section reveals a floating button. When clicked, a mini popup appears with the option to either start a new chat with a friend the user already has, or to add to a new friend from the list of total pre-existing users of the app.
**Note:** You may not add yourself, add a user that doesn't exist or add a person you are already friends with.
```

beepr.db is a database file containing three tables; A users table, friends table, and messages table


Below is the structure of the files in the database
#### users
|               |      id       | name          | username     |     email     | password_hash|      bio      |
| ------------- | ------------- | ------------- |------------- | ------------- |------------- | ------------- |
| **data type** |     TEXT      |     TEXT      |  TEXT UNIQUE |  TEXT UNIQUE  |     TEXT     |  TEXT UNIQUE  |

#### friends
|               |    user_id    |   friends_id  | username     |     email     | password_hash|      bio      |
| ------------- | ------------- | ------------- |------------- | ------------- |------------- | ------------- |
| **data type** |     TEXT      |     TEXT      |  TEXT UNIQUE |  TEXT UNIQUE  |     TEXT     |  TEXT UNIQUE  |

#### messages
|               |  sender_id    |  receiver_id  |  message     |     email     | password_hash|      bio      |
| ------------- | ------------- | ------------- |------------- | ------------- |------------- | ------------- |
| **data type** |     TEXT      |     TEXT      |  TEXT UNIQUE |  TEXT UNIQUE  |     TEXT     |  TEXT UNIQUE  |
