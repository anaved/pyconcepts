'''
Created on Feb 4, 2014

@author: Naved
Abstract classes are used to define API. 
By declaring a method abstract, parent class can enforce the child to implement the method before
being able to instantiate.
'''

import abc
#if you remove meta class, abstract will have no affect
class MyAbstract(object):
    __metaclass__=abc.ABCMeta
    @abc.abstractmethod
    def my_print(self):
        pass

class MyConcrete(MyAbstract):
    def my_print(self):
        print "tada"
    

m=MyConcrete()
m.my_print()
