'''
Created on 04-Feb-2014

@author: naved
'''
''
# A simple test with mixin
class MyMixin1(object):
    def pdispatch(self):
        print self.data+" mixin-1"

class MyMixin2(object):
    def pdispatch(self):
        print self.data+" mixin-2"
    

class MixinCaller(MyMixin1,MyMixin2):
    def __init__(self,data):
        self.data=data
        
    def pdata(self):
        self.pdispatch()
        print self.data

d=MixinCaller("data")
d.pdispatch()
d.pdata()