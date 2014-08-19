'''
Created on Feb 4, 2014

@author: Naved
'''
class MyIterable(object):

    def __init__(self,number):
        self.number=number
        
    def __iter__(self):
        return self

    def next(self):
        self.number=self.number+1
        return self.number
    
    
mi=MyIterable(1)
print mi.next()
print mi.next()
print mi.next()
print mi.next()
print mi.next()
print mi.next()    