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
          {'type': 'WORK', 'number': '999999999'}, 
          {'type': 'HOME', 'number': '999999999'}
        ]
        email = 'leoisso.work@gmail.com'

        file = open('./test/mock/test_img.png', 'rb')
        image = file.read()
        file.close()
        self.encoded_image = encode_image_file(image)
        
        self.assembler = VCFAssembler2(name, phones, email, image)

    def test_set_review(self):
        self.assembler.set_review()
        result = f'\nREV:{self.assembler.revision}'
        self.assertEqual(self.assembler.vcf_body, result)

    def test_set_phones(self):
        result = f'\nTEL;WORK;VOICE:999999999\nTEL;HOME;VOICE:999999999'
        self.assembler.set_phones()
        self.assertEqual(self.assembler.vcf_body, result)

    def test_set_image(self):
        result = f'\nPHOTO;JPEG;ENCODING=BASE64:{self.encoded_image}'
        self.assembler.set_image()
        self.assertEqual(self.assembler.vcf_body, result)

if __name__ == "__main__":
    unittest.main()