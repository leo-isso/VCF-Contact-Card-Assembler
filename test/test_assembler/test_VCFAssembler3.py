from assembler.VCFAssembler3 import VCFAssembler3
from image_encoder.image_encoder import encode_image_file

import unittest

class TestVCFAssembler3(unittest.TestCase):
    
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
        
        self.assembler = VCFAssembler3(name, phones, email, image)

    def test_set_version(self):
        result = f'\nVERSION:3.0'
        self.assembler.set_version()
        self.assertEqual(self.assembler.vcf_body, result)

    def test_set_name(self):
        result = '\nN:Isso;Leonardo;;Mr.;\nFN:Isso Leonardo'
        self.assembler.set_name()
        self.assertEqual(self.assembler.vcf_body, result)

    def test_set_email(self):
        result = '\nEMAIL:leoisso.work@gmail.com'
        self.assembler.set_email()
        self.assertEqual(self.assembler.vcf_body, result)

    def test_set_review(self):
        self.assembler.set_review()
        result = f'\nREV:{self.assembler.revision}'
        self.assertEqual(self.assembler.vcf_body, result)

    def test_set_phones(self):
        result = f'\nTEL;TYPE=WORK,VOICE:999999999\nTEL;TYPE=HOME,VOICE:999999999'
        self.assembler.set_phones()
        self.assertEqual(self.assembler.vcf_body, result)

    def test_set_image(self):
        result = f'\nPHOTO;JPEG;ENCODING=b:{self.encoded_image}'
        self.assembler.set_image()
        self.assertEqual(self.assembler.vcf_body, result)

    def test_build_vcf_body(self):
        self.assembler.build_vcf_body()
        result = f'BEGIN:VCARD\nVERSION:3.0\nN:Isso;Leonardo;;Mr.;\nFN:Isso Leonardo\nEMAIL:leoisso.work@gmail.com\nTEL;TYPE=WORK,VOICE:999999999\nTEL;TYPE=HOME,VOICE:999999999\nPHOTO;JPEG;ENCODING=b:{self.encoded_image}\nREV:{self.assembler.revision}\nEND:VCARD'
        self.assertEqual(self.assembler.vcf_body, result)

if __name__ == "__main__":
    unittest.main()