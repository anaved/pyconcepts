'''
Created on Feb 4, 2014

@author: Naved
'''

running_cat = type('Cat', (object,), {'meow': 'Meow',
                                    'eat': 'Eat',
                                    'sleep': 'Sleep'})

print running_cat
print running_cat.meow