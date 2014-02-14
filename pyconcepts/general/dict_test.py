'''
Created on Feb 4, 2014

@author: Naved
'''
class A(object):
    def __init__(self,name):
        self.name=name
    

my_dict={}
my_dict[A('naved')]='naved'
my_dict[A('naved')]='naved'

print my_dict.items()

my_dict[(1,2,3)]='naved'

print my_dict.items()

