'''
Created on Feb 4, 2014

@author: Naved
'''
import thread

def test():
    print "hello world!"

thread.start_new_thread(test,())
thread.start_new_thread(test,())
