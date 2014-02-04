'''
Created on 04-Feb-2014

@author: naved
'''
''
#A way to provide access methods to change any attribute of a class
# There are inheritence friendly 
 
class MyProperty(object):
    def __init__(self,name):
        self.name=name
    @property
    def xname(self):
        return self.name
    
    @xname.setter
    def xname(self,val):
        self.name=val
    
    @xname.deleter
    def xname(self):
        del self.name


class MyOtherProperty(object):
    def __init__(self,name):
        self.name=name
    
    def getXName(self):
        return self.name    
    
    def setXName(self,val):
        self.name=val
    
    
    def deleteXName(self):        
        del self.name
 
        
    xname=property(getXName,setXName,deleteXName,"here is all the doc you want")


mo=MyOtherProperty('naved')
print mo.xname
mo.xname="test"
print mo.xname
del mo.xname
print mo.xname