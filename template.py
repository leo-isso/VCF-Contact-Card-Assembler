"""
high level support for doing this and that.
"""

TEMPLATE = '''BEGIN:VCARD
VERSION:2.1
{};{};;{}.
FN:{}
ORG:{}
TITLE:{}
PHOTO;GIF:{}
TEL;WORK;VOICE:{}
TEL;HOME;VOICE:{}
TEL;CELL;VOICE:{}
EMAIL:{}
REV:{}
END:VCARD'''

print(TEMPLATE)
