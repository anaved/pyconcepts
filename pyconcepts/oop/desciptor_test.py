'''
Created on 04-Feb-2014

@author: naved
'''
''
# A way to intercept attribute access
# These are more composition friendly
  
class MyDescriptorClass(object):
        
    def __get__(self,instance,owner):
        print instance,owner
        return instance._name

    def __set__(self,instance,value):
        print instance
        instance._name=value    
    def __delete__(self,instance):        
        del instance._name
            

class MyCallerClass(object):
    def __init__(self, name):
        self._name=name
    name=MyDescriptorClass()

class OtherCallerClass(object):
    def __init__(self, name):
        self._name=name
    name=MyDescriptorClass()
    
bob=MyCallerClass('Bob')
print bob.name
bob.name="Naved"
print bob.name
del bob.name

bob=OtherCallerClass('Boon')
print bob.name
bob.name="Naved"
print bob.name
del bob.name 