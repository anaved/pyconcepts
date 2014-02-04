'''
Created on Feb 5, 2014

@author: Naved
'''
def quicksort(array):
    if not array:
        return []
    pivot=array[0]
    less=quicksort([x for x in array[1:] if x<pivot])
    great=quicksort([x for x in array[1:] if x>=pivot])
    return less+[pivot]+great

print quicksort([9,8,8,7])