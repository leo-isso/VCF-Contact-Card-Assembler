"""
    This script filters user's inputs
"""

from dialogs import *

def mainMenuFilter(input_data):
    if input_data == 'help':
        print(MSG_HELP)
        return True
    elif input_data == 'commands':
        print(MSG_CMDLIST)
        return True
    elif input_data == 'credits':
        print(MSG_CREDITS)
        return True
    elif input_data == 'version':
        print(MSG_VERSION)
        return True
    else:
        return False
