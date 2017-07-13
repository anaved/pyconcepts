'''
Created on Feb 4, 2014

@author: Naved
'''
from functools import wraps

def decorator(func):
    """
    :param func:
    :return: func result after calling it with 1
    """
    return func(1)

#Below statement is equal to decorator( decoratee )
@decorator
def decoratee(number):
    """
    :param number:
    :return: number + 1
    """
    return number + 1

from functools import wraps
def memoize(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            print 'Running func'
            cache[args] = func(*args)
        else:
            print 'result in cache'
        return cache[args]
    return wrap

@memoize
def myfunc(a):
    return a**2

def decorator2(func):
    """
    :param func:
    :return: function wrapper
    """
    def wrapper(number):
        number = number + 1
        return func(number)
    return wrapper

@decorator2
def decoratee2(number):
    """
    :param number:
    :return: number + 1
    """
    return number + 1



if __name__ == "__main__":

    print decoratee2(1)
#>>> 3
    print decoratee2(2)
#>>> 4