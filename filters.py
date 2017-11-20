"""
    This script filters user's inputs
"""

from dialogs import *

def mainMenuFilter(input_data):
    if input_data == 'help':
        print(MSG_HELP)
    elif input_data == 'commands':
        print(MSG_CMDLIST)
    elif input_data == 'credits':
        print(MSG_CREDITS)
    elif input_data == 'version':
        print(MSG_VERSION)
    else:
        print(MSG_CMDERROR)
