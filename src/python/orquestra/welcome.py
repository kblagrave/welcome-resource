"""
This module saves a welcome message
"""

import json

def welcome():
    message = "Welcome to Orquestra."
    message_dict = {'message': message,'schema':'message'}
    # save output to file so it can be passed on or accessible at end
    with open('welcome.json,'w') as f:
        f.write(json.dumps(message_dict, indent=2))
