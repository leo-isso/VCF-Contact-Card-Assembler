"""
    This script contains the user dialogs
"""

MSG_START = 'Welcome to VCF Contact Card Assembler'
MSG_HELP = '''This script compose, decompose, read and edit vCards in (.vcf) extension.
(Use "commands" to see the command list.)
'''
MSG_INPUT = '>>> '
CMD_LIST = [
    'new_contact',
    'new_contactlist'
    'edit_contact',
    'edit_contactlist',
    'read_contact',
    'read_contactlist',
    'commands',
    'version',
    'credits']
MSG_CMDLIST = '''
"new_contact"           Create new single contact vCard
"new_contactlist"       Create new contact list vCard
"edit_contact"          Edit single contact vCard
"edit_contactlist"      Edit contact list vCard
"read_contact"          Read single contact vCard
"read_contactlist"      Read contact list vCard
"commands"              Show command list
"version"               Show the script version
"credits"               Show the credits
'''
MSG_CMDERROR = '''
The command is invalid, try again.
(Use "commands" to see the command list.)
'''
MSG_CREDITS = '''
Author: Leonardo Isso
<leoisso.work@gmail.com>
https://leonardoisso.com.br/
'''
MSG_VERSION = '1.0.0'
MSG_INPUT_ERROR = 'Invalid input, try again'

#newContact MSG
MSG_NEWCONTACT_START = 'New contact creation:'
MSG_NEWCONTACT_VERSION = 'vCard Version[2.1 or 3.0(recommended)]: '
