import unittest
import source

class TestCalc(unittest.TestCase):
    def testSub(self):
        self.assertEqual(1, source.performSub(2, 1),
         "Bug in Subtractor. Results should be 1.")

    def testmMult(self):
        self.assertEqual(2, source.performMult(2, 1),
         "Bug in Multiplier. Results should be 2.")

    def testDiv(self):
        self.assertEqual(5, source.performSub(10, 2),
         "Bug in Divider. Results should be 5.")

if __name__ == '__main__':
    unittest.main()