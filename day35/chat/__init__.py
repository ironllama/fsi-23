from flask import Flask

app = Flask(__name__)

# This file is pretty stark now, but it can contain any configuration
#  or logic that pertains to the app/service/server as a whole.

# import chat.views1  # This will contain logic about each endpoint.
# import chat.views2  # This will contain logic about each endpoint.
# import chat.views3  # This will contain logic about each endpoint.
import chat.views4  # This will contain logic about each endpoint.