"""
    This script encodes IMAGE FILES* into base64

    *IMAGE FILES = JPG and PNG
"""

import base64

B64_STRING = '' #encoded base64 string

def encodeImage(file_location):
    file = open(file_location, 'rb')
    image_file = file.read()
    file.close()
    encoded_string = base64.b64encode(image_file)
    return encoded_string

def decodeImage():
    '''
        Not used in this app, but you can use to see which image is being built
    '''
    string = B64_STRING
    byte_string = base64.b64decode(string)
    file = open('build.jpg', 'wb')
    file.write(byte_string)
    file.close()
