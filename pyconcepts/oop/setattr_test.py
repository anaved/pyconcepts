'''
Created on Feb 4, 2014

@author: Naved
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