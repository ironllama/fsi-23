from flask import render_template, request
from chat import app
from datetime import datetime

# The "/" route will send the UI.
@app.get("/")
def home():
    return render_template("chat4.html")


# Authentication. If the user exists, validate the password.
# If not, just create the new user.
@app.post("/auth")
def auth():
    # Read all incoming JSON data, do some validation
    user = request.json.get('user', '')
    password = request.json.get('pass', '')
    if user == '' or password == '':
        return { 'message': 'User and pass are required.'}

    # Check user/pass file to see if the user exists    
    with open('chat/auth.db', 'r', encoding='utf-8') as f:
        all_lines = [line.strip().split("|") for line in f.readlines()]
        all_lines = {line[0]: line[1] for line in all_lines}

    if user in all_lines:
        # User exists, check password
        if password == all_lines.get(user):
            return { 'message': 'OK' }
        else:
            return { 'message': 'Invalid username or password!'}
    else:
        # New user, write into db
        new_line = f"{user}|{password}\n"

        with open('chat/auth.db', 'a', encoding='utf-8') as f:
            f.write(new_line)

        return { 'message': 'OK' }
    

# For each new message that the UI sends to add to the chat history.
@app.post("/new_message")
def new_message():
    # Read all incoming JSON data, do some validation
    user = request.json.get('user', '')
    text = request.json.get('text', '')
    if user == '' or text == '':
        return { 'message': 'User and text are required.'}

    time = datetime.now().strftime("%Y-%m-%d %I:%M:%S%p")
    time.replace(" 0", "")  # Hacky way to remove leading 0 from hour

    # What each line will look like: a pipe(|) delimited sequence of data.
    new_line = f"{user}|{time}|{text}\n"

    with open('chat/allchats.db', 'a', encoding='utf-8') as f:
        f.write(new_line)

    return { 'message': 'OK' }


# Get a list of all the messages (JSON)
@app.get("/all_messages")
def all_messages():
    with open('chat/allchats.db', 'r', encoding='utf-8') as f:
        all_lines = f.readlines()
    
    # Convert each line from a string into a list.
    all_lines = [line.strip().split("|") for line in all_lines] 

    # Covert each line from a list into a dictionary.
    all_chats = [{'user': line[0], 'time': line[1], 'text': line[2]} for line in all_lines]

    return all_chats
