'''
Created on Feb 4, 2014

@author: Naved
'''

import threading
class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()
    
    def run(self):
        print "tada"
        threading.Lock.acquire()
        print "done"
        threading.Lock.release()
threadlist=[]
for e in xrange(0,10):        
    a=MyThread()
    a.start()
    threadlist.append(a)
for thread in threadlist:
    thread.join()
        
    