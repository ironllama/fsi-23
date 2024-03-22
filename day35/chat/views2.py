from flask import render_template, request
from chat import app
from datetime import datetime

# The "/" route will send the UI.
# We're going to preload all the messages from chat history into the UI.
@app.get("/")
def home():
    with open('chat/allchats.db', 'r', encoding='utf-8') as f:
        all_lines = f.readlines()
    
    # Convert each line from a string into a list.
    all_lines = [line.strip().split("|") for line in all_lines] 

    # Covert each line from a list into a dictionary.
    all_chats = [{'user': line[0], 'time': line[1], 'text': line[2]} for line in all_lines]

    return render_template("chat2.html", all_chats=all_chats)


# For each new message that the UI sends to add to the chat history.
@app.post("/new_message")
def new_message():
    # Read all incoming JSON data, do some validation
    user = request.json.get('user', '')
    text = request.json.get('text', '')
    if user == '' or text == '':
        return { 'message': 'User and text are required.'}

    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S%p")
    time.replace(" 0", "")  # Hacky way to remove leading 0 from hour

    # What each line will look like: a pipe(|) delimited sequence of data.
    new_line = f"{user}|{time}|{text}\n"

    with open('chat/allchats.db', 'a', encoding='utf-8') as f:
        f.write(new_line)

    return { 'message': 'OK' }