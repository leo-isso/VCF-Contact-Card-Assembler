"""
    This script interacts with user to gather, save and edit vCards data.
"""

import VCFAssembler
import filemanager

from dialogs import *

def cancelCore():
    pass

def newContact():
    contact = VCFAssembler.ContactAssembler()
    print(MSG_NEWCONTACT_START)
    

if __name__ == '__main__':
    newContact()
