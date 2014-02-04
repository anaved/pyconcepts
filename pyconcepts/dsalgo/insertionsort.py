'''
Created on Feb 5, 2014

@author: Naved
'''
def insertion(array):
    for e,v in enumerate(array[:-1]):
        for f,j in enumerate(array[1:]):            
            if v>j:
                temp=j
                array[f]=v
                array[e]=temp
                e=f                
    return array
 
print insertion([9,8,7,5])

    