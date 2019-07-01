from assembler.VCFAssembler2 import VCFAssembler2
import unittest


class TestVCFAssembler2(unittest.TestCase):
    
    def setUp(self):
        version = '3.0'
        name = {
            'name': 'Leonardo',
            'surname': 'Isso',
            'treatment': 'Mr.'
        }
        email = 'leoisso.work@gmail.com'

        self.assembler = VCFAssembler2(version, name, email=email)

    def test_set_review(self):
        self.assembler.set_review()
        result = f'\nREV:{self.assembler.revision}'
        self.assertEquals(self.assembler.vcf_body, result)

if __name__ == "__main__":
    unittest.main()