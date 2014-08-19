'''
Created on Feb 4, 2014

@author: Naved
'''
def gentest(limit):
    for i in xrange(limit):
        yield i+1

g= gentest(5)
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
