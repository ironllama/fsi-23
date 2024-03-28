from flask import request, session, redirect, url_for, render_template
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError

from chat import app, sql

def check_logged_in():
    if session.get('user', ''):
        return True
    else:
        return redirect(url_for('home'))


@app.route("/auth")
def home():
    return app.send_static_file("auth.html")


@app.get("/chat")
def chat():
    check_logged_in()
    return render_template("chat.html", user=session['user'])


@app.post("/login")
def login():
    params = {
        'login': request.form.get("username", ''),
        'pass': request.form.get("password", '')
    }

    for field in params:
        if field == '':
            return redirect(url_for('home'))

    with sql.connect() as conn:
        res = conn.execute(
            text("SELECT 1 FROM chatusers WHERE login=:login AND password=:pass"),
            params,
            execution_options={ 'preserve_rowcount': True }  # NEW! Allows for rowcount in SELECT, INSERT
        )
        if res.rowcount > 0:
            session['user'] = params['login']  # Add user name to session
            return redirect(url_for('chat'))
        else:
            session.pop('user', None)
            return redirect(url_for('home'))


@app.post("/signup")
def signup():
    params = {
        'login': request.form.get("username", ''),
        'pass': request.form.get("password", ''),
        'email': request.form.get("email", '')
    }

    for field in params:
        if field == '':
            return redirect(url_for('home'))

    try:
        with sql.begin() as conn:
            res = conn.execute(
                text("INSERT INTO chatusers (login, password, email) VALUES (:login, :pass, :email)"),
                params
            )
            session['user'] = params['login']  # Add user name to session
            return redirect(url_for('chat'))
    except SQLAlchemyError as e:
        print("signup: ERROR:", str(e.orig))


@app.get("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))


# For each new message that the UI sends to add to the chat history.
@app.post("/new_message")
def new_message():
    check_logged_in()
    
    # Read all incoming JSON data, do some validation
    params = {
        'login': session.get("user", ''),
        'message': request.json.get("text", '')
    }

    for field in params:
        if field == '':
            return { 'message': 'User and text are required.' }

    # What each line will look like: a pipe(|) delimited sequence of data.
    try:
        with sql.begin() as conn:
            conn.execute(
                text("INSERT INTO chatmessages (user_id, message) VALUES ((SELECT id FROM chatusers WHERE login=:login), :message)"),
                params
            )
            return { 'message': 'OK' }
    except SQLAlchemyError as e:
        print("signup: ERROR:", str(e.orig))


# Get a list of all the messages (JSON)
@app.get("/all_messages")
def all_messages():
    check_logged_in()

    with sql.connect() as conn:
        res = conn.execute(text("SELECT login, message, created_date FROM chatmessages m JOIN chatusers u ON user_id = u.id"))

        all_chats = []
        for row in res:
            all_chats.append({
                'user': row.login,
                'text': row.message,
                'time': row.created_date
            })
        return all_chats
