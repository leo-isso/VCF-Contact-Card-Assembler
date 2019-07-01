from assembler.VCFAssembler import VCFAssembler
import unittest


class TestVCFAssembler(unittest.TestCase):
    
    def setUp(self):
        version = '3.0'
        name = {
            'name': 'Leonardo',
            'surname': 'Isso',
            'treatment': 'Mr.'
        }

        self.assembler = VCFAssembler(version, name)

    def test_set_version(self):
        result = """\nVERSION:3.0"""
        self.assembler.set_version()
        self.assertEquals(self.assembler.vcf_body, result)

    def test_set_name(self):
        result = """\nN:Isso;Leonardo;;Mr.;\nFN:Isso Leonardo"""
        self.assembler.set_name()
        self.assertEquals(self.assembler.vcf_body, result)


if __name__ == "__main__":
    unittest.main()