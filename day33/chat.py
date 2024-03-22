# 1. You are going to create a chat web app. The web app includes:
#    - an input to identify the person chatting
#    - an area to display the current messages
#    - an input to enter a new message

#    Anytime the page is loaded, it should retrieve all the messages from
#     the backend.

#    Messages are sent to the backend and stored in a file in any format.
#     You must store at least the date/time the message was sent, the name
#     of the message sender, and the message text for every message.

#    A user can not send a new message if the user did not identify
#     themselves. (If they did not provide a name.)

#    Once a message is sucessfully sent, refresh the page to retrieve the
#     new messages, including the one that was just sent.


# 2. Having to manually refresh the chat page is not great -- you might
#     forget to refresh the page and end up missing messages! Put your web
#     app on a resonable automatic reloading period so that it will do the
#     page reloads without user intervention.


# 3. Page reloads has its own drawbacks. For example, while you were typing
#    a new message into the input, a page refresh would reset the input. So,
#    change the way the page works by using AJAX to get all the messages
#    from the backend and refresh only the current messages area of your web
#    app. The page itself should NOT refresh. 


# 4. Create a rudimentary authentication system for your chat app where you
#     allow the user to create a new account on your system, and then they
#     can use the username/password to login at any time in the future.
#     Don't worry about security (hashing passwords, encryption, etc.) for
#     now -- just get a system to work. (Obviously, since all the passwords
#     are going to be in plain text, don't use any real passwords you use
#     in real life.)
#
#    Once you get a system working, you can go back and figure out how you
#     would want to change things to make things more secure. Feel free to
#     discuss with the instructor or others in the class.
