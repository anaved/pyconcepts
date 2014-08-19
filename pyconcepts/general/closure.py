'''
Created on Feb 4, 2014

@author: Naved
'''
# its a function with data associated
def outer(limit):
    def inner(start):
        return limit+start
    return inner
x=outer(4)
print x(5)
print x(15)


