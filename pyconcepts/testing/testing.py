'''
Created on Feb 3, 2014

@author: Naved
'''
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        self.data=[1,2,3,'4',5.14,'naved']
    def testInteger(self):
        pass
    def testString(self):
        pass
    def testFloat(self):
        for e in self.data:
            self.assertIsInstance(e, str)

if __name__=='__main__':
    unittest.main()
        