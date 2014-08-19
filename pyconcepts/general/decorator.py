'''
Created on Feb 4, 2014

@author: Naved
'''
# its a function working as a decorator
def dec_test(test_meth):
    return test_meth(1)
@dec_test
def my_meth(number):
    return number+1

# print my_meth(1)
    
dec_test(my_meth())