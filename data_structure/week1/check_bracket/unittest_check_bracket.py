import unittest
from check_bracket import find_mismatch


class Test_find_mismatch(unittest.TestCase):
    def test_small(self):
        self.assertEqual( find_mismatch(" "), "Success")
        
        self.assertEqual( find_mismatch("{[]}()"), "Success")
        self.assertEqual( find_mismatch("{[}"), 3)
        self.assertEqual( find_mismatch("{[}"), 3)
        self.assertEqual( find_mismatch("foo(bar);"), 'Success')

        self.assertEqual( find_mismatch( "foo(bar);"*100 ), 'Success')
        self.assertEqual( find_mismatch( "{[]}()"*100 ), "Success")
        
        self.assertEqual( find_mismatch( "{x[]}foo()"*1000 + '{' ), 10001)

        self.assertEqual( find_mismatch( "{x[]}foo()"*1000 + '{' + "{x[]}foo()"*1000), 10001)

if __name__ == '__main__':
    unittest.main()