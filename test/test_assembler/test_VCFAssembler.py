from assembler.VCFAssembler import VCFAssembler

import unittest

class TestVCFAssembler(unittest.TestCase):
    
    def setUp(self):
        name = {
            'name': 'Leonardo',
            'surname': 'Isso',
            'treatment': 'Mr.'
        }
        email = 'leoisso.work@gmail.com'

        self.assembler = VCFAssembler(name, email=email)

    def test_set_version(self):
        result = f"""\nVERSION:{self.assembler.version}"""
        self.assembler.set_version()
        self.assertEqual(self.assembler.vcf_body, result)

    def test_set_name(self):
        result = """\nN:Isso;Leonardo;;Mr.;\nFN:Isso Leonardo"""
        self.assembler.set_name()
        self.assertEqual(self.assembler.vcf_body, result)

    def test_set_email(self):
        result = """\nEMAIL:leoisso.work@gmail.com"""
        self.assembler.set_email()
        self.assertEqual(self.assembler.vcf_body, result)

    def test_build_vcf_body(self):
        result = """BEGIN:VCARD\nVERSION:3.0\nN:Isso;Leonardo;;Mr.;\nFN:Isso Leonardo\nEMAIL:leoisso.work@gmail.com\nEND:VCARD"""
        self.assembler.build_vcf_body()
        self.assertEqual(self.assembler.vcf_body, result)

if __name__ == "__main__":
    unittest.main()