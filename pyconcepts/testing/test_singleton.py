'''
Created on Jan 2, 2014

@author: Naved
@summary: Module to test a singleton generation behaviur in python
        Condition to be tested
            1- The object is created
            2- There are no duplicates of the object
'''
from designs.singleton import MySingleton
import unittest

class MyOrdinary(object):
    pass

class SingletonTestCase( unittest.TestCase ):
    def setUp(self):
        self.singleton=MySingleton()
        self.ordinary=MyOrdinary()
    def test_singletonCreated( self ):
        '''
        Check if object is instance of the MySingleton
        '''
        self.assertIsInstance( self.singleton , MySingleton )
    
    def test_singletonUnique( self ):
        '''
        Check if both the objects are equal
        '''
        oneMoreInstance= MySingleton()
        self.assertIs(self.singleton,oneMoreInstance)
               
    def test_ordinaryNonUnique( self ):
        oneMoreOrdinary=MyOrdinary()
        self.assertIsNot(self.ordinary, oneMoreOrdinary)   

if __name__ == '__main__':
    unittest.main() 