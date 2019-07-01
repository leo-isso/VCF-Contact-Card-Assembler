from assembler.VCFAssembler2 import VCFAssembler2
from image_encoder.image_encoder import encode_image_file

import unittest

class TestVCFAssembler2(unittest.TestCase):
    
    def setUp(self):
        name = {
            'name': 'Leonardo',
            'surname': 'Isso',
            'treatment': 'Mr.'
        }
        phones = [
          {'type': 'TEL', 'number': '999999999'}, 
          {'type': 'CEL', 'number': '999999999'}
        ]
        email = 'leoisso.work@gmail.com'

        file = open('./test/mock/test_img.png', 'rb')
        image = file.read()
        file.close()

        self.assembler = VCFAssembler2(name, phones, email, image)

    def test_set_review(self):
        self.assembler.set_review()
        result = f'\nREV:{self.assembler.revision}'
        self.assertEqual(self.assembler.vcf_body, result)

    def test_set_phones(self):
        result = f'\nTEL;TEL;VOICE:999999999\nTEL;CEL;VOICE:999999999'
        self.assembler.set_phones()
        self.assertEqual(self.assembler.vcf_body, result)

    def test_set_image(self):
        encoded_image = encode_image_file(self.assembler.image)
        result = f'\nPHOTO;JPEG;ENCODING=BASE64:{encoded_image}'
        self.assembler.set_image()
        self.assertEqual(self.assembler.vcf_body, result)

if __name__ == "__main__":
    unittest.main()