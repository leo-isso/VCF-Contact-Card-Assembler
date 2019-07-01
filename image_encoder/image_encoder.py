"""
    This script encodes IMAGE FILES* into base64

    *IMAGE FILES = JPG and PNG
"""

import base64

def encode_image_file(file):
    encoded_string = base64.b64encode(file)
    encoded_string = encoded_string.decode('utf-8')
    return encoded_string