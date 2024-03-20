# Create a flask server that will act as an API and have these endpoints:
# - /numvowels
#    This endpoint accepts the GET method and expects to have an argument
#    called 'word'. It will return the number of vowels in the word.
# - /greetings
#    This endpoint accepts the POST method and expects to have an argument
#    called 'name' sent in url-encoded form data. It will return a string
#    in the format: "Hello <name>, your name backwards is <name backwards>!"
# - /dateinfo
#    This endpoint accepts GET or POST and expects to have the arguments
#    sent in via JSON, with a property called 'date' in the format
#    'yyyy-mm-dd'. This endpoint will return a JSON string with the date
#    parsed out into properties for year, month name (not number), day of
#    month, day of week, and day of year.
# - /user/<user_id>
#    This endpoint accepts the GET method and expects to have an argument
#    called 'snack'. If the user_id is '123-456-7890', return a JSON
#    string with a 'message' property and value of "<user_id> loves to eat
#    <snack>s", otherwise the message will be "User not found."
#
# Also, create a web page with HTML forms with appropriate inputs for
# each of the above API endpoints. Use JS to handle form submissions,
# as necessary. Remember to also use the appropriate request methods
# and data formats to match what is expected from the API. Display results
# of each API call below the respective forms.
from flask import Flask, request
from datetime import date

app = Flask(__name__)

@app.get("/numvowels")
def numvowels():
    word = request.args.get('word', '')
    return str(len([char for char in word if char.lower() in "aeiou"]))

@app.post("/greetings")
def greetings():
    name = request.form.get('name', '')
    return f"Hello {name}, your name backwards is {name[::-1]}!"

@app.route("/dateinfo", methods=['GET', 'POST'])
def dateinfo():
    if request.method == 'GET':
        date_str = request.args.get('date', '')
    else:
        date_str = request.form.get('date', '')

    if date_str:
        date_val = date.fromisoformat(date_str)
    else:
        date_val = date.today()
    
    return {
        "year": date_val.year,
        "month": date_val.strftime("%B"),
        "day": date_val.day,
        "weekday": date_val.strftime("%A"),
        "yearday": date_val.strftime("%j"),
    }

@app.get("/user/<user_id>")
def user(user_id):
    snack = request.args.get('snack', '')
    if user_id == '123-456-7890':
        return { "message": f"{user_id} loves to eat {snack}{'s' if not snack.endswith('s') else ''}." }
    else:
        return { "message": "User not found." }