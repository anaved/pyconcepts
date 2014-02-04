'''
Created on Feb 5, 2014

@author: Naved
'''
def reverse(x):
    if not len(x)>1:
        return x
    else:
        return x[-1]+reverse(x[1:-1])+x[0]
    
print reverse("naved")    