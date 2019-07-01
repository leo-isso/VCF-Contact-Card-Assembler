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

        self.assemble = VCFAssembler(version, name)

    def test_set_version(self):
        result = """\nVERSION:3.0"""
        self.assemble.set_version()
        self.assertEquals(self.assemble.vcf_body, result)

    def test_set_name(self):
        result = """\nN:Isso;Leonardo;;Mr.;\nFN:Isso Leonardo"""
        self.assemble.set_name()
        self.assertEquals(self.assemble.vcf_body, result)


if __name__ == "__main__":
    unittest.main()