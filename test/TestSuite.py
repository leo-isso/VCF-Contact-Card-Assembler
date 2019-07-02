import unittest
from test.test_assembler.test_VCFAssembler import TestVCFAssembler
from test.test_assembler.test_VCFAssembler2 import TestVCFAssembler2

suite_VCFAssembler = unittest.TestLoader().loadTestsFromTestCase(TestVCFAssembler)
suite_VCFAssembler2 = unittest.TestLoader().loadTestsFromTestCase(TestVCFAssembler2)

all_tests = unittest.TestSuite([suite_VCFAssembler,
                              suite_VCFAssembler2])

unittest.TextTestRunner().run(all_tests)