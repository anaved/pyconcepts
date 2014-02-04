'''
Created on Feb 5, 2014

@author: Naved
'''
# Laws of recursion
# 1- The method should call itself
# 2- There has to be an end/break condition
# 3- Program should always progress towards end condition

#febonacci
def febonacci(number):
    if number==0 or number==1:
        return 1   
    return febonacci(number-1)+febonacci(number-2) 

#factorial
def factorial(number):
    if number==0:
        return 1
    return number*factorial(number-1)

print factorial(5)
print febonacci(4)
