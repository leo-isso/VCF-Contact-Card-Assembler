import unittest
from test.test_assembler.test_VCFAssembler2 import TestVCFAssembler2
from test.test_assembler.test_VCFAssembler3 import TestVCFAssembler3

suite_VCFAssembler2 = unittest.TestLoader().loadTestsFromTestCase(TestVCFAssembler2)
suite_VCFAssembler3 = unittest.TestLoader().loadTestsFromTestCase(TestVCFAssembler3)

all_tests = unittest.TestSuite([suite_VCFAssembler2, suite_VCFAssembler3])

unittest.TextTestRunner().run(all_tests)