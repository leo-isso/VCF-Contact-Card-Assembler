"""
    This script contains the template file formats and its versions
"""
"""
TEMPLATE_2_1 = f'''BEGIN:VCARD
VERSION:2.1
{};{};;{}.
FN:{}
ORG:{}
TITLE:{}
PHOTO;{}:{}
TEL;WORK;VOICE:{}
TEL;HOME;VOICE:{}
TEL;CELL;VOICE:{}
EMAIL:{}
REV:{}
END:VCARD'''

TEMPLATE_3_0 = f'''BEGIN:VCARD
VERSION:3.0
N:{};{};;{};
FN:{}
ORG:{}
TITLE:{}
PHOTO;VALUE={};TYPE={}:{}
TEL;TYPE={},VOICE:{}
TEL;TYPE={},VOICE:{}
ADR;TYPE={},PREF:;;{}
LABEL;TYPE={},PREF:100 Waters Edge\nBaytown\, LA 30314\nUnited States of 
ADR;TYPE={}:;;42 Plantation St.;Baytown;LA;30314;United States of America
LABEL;TYPE={}:42 Plantation St.\nBaytown\, LA 30314\nUnited States of Ame
EMAIL:{}
REV:{}T{}Z
END:VCARD''' #MOST USED (2016-NOW)
"""

TEMPLATE_TESTE = '''BEGIN:VCARD
VERSION:3.0
N:Gump;Forrest;;Mr.;
FN:Forrest Gump
ORG:Bubba Gump Shrimp Co.
TITLE:Shrimp Man
PHOTO;VALUE=URI;TYPE=GIF:http://www.example.com/dir_photos/my_photo.gif
TEL;TYPE=WORK,VOICE:(111) 555-1212
TEL;TYPE=HOME,VOICE:(404) 555-1212
ADR;TYPE=WORK,PREF:;;100 Waters Edge;Baytown;LA;30314;United States of Amer
LABEL;TYPE=WORK,PREF:100 Waters Edge\nBaytown\, LA 30314\nUnited States of 
ADR;TYPE=HOME:;;42 Plantation St.;Baytown;LA;30314;United States of America
LABEL;TYPE=HOME:42 Plantation St.\nBaytown\, LA 30314\nUnited States of Ame
EMAIL:forrestgump@example.com
REV:2008-04-24T19:52:43Z
END:VCARD
'''
