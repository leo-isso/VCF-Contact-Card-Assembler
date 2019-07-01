from assembler.VCFAssembler2 import VCFAssembler2
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

        self.assembler = VCFAssembler2(name, phones, email)

    def test_set_review(self):
        self.assembler.set_review()
        result = f'\nREV:{self.assembler.revision}'
        self.assertEquals(self.assembler.vcf_body, result)

    def test_set_phones(self):
        result = f'\nTEL;TEL;VOICE:999999999\nTEL;CEL;VOICE:999999999'
        self.assembler.set_phones()
        self.assertEquals(self.assembler.vcf_body, result)


if __name__ == "__main__":
    unittest.main()