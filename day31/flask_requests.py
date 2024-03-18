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