'''
Created on 04-Feb-2014

@author: naved
'''
''
# A way to provide access methods to change any attribute of a class
# There are inheritence friendly 
import abc

class MyPropertyValidation(object):
    def __init__(self):
        self.__age = None

    @property
    def age(self):
        if not self.__age:
            raise ValueError("Age is None and needs to be set first.")
        return self.__age

    @age.setter
    def age(self, val):
        if isinstance( val, int ) and val > 0:
            self.__age = val
        else:
            raise ValueError("Age needs to be an integer and greater than zero")



class MyProperty(object):
    def __init__(self, name):
        self.__name = name

    @property
    def xname(self):
        return self.__name

    @xname.setter
    def xname(self, val):
        self.__name = val

    @xname.deleter
    def xname(self):
        del self.__name

class MyOtherProperty(object):
    def __init__(self, name):
        self.name = name

    def getXName(self):
        return self.name

    def setXName(self, val):
        self.name = val

    def deleteXName(self):
        del self.name

    xname = property(getXName, setXName, deleteXName, "here is all the doc you want")


class MyAbstractProperty(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def xname(self): pass


class MyAbstractPropertySubclass(MyAbstractProperty):
    @property
    def xname(self):
        return 1


class MyFinalProperty(object):

    @property
    def name(self):
        return "John"

if __name__ == '__main__':
    # #Instantiate class with initial value
    # myProp = MyProperty("John")
    # #Print initial value
    # print myProp.xname
    # #Update value
    # myProp.xname = "Doe"
    # #Print updated value
    # print myProp.xname
    # #Delete property
    # del myProp.xname
    # #This will raise exception
    # print myProp.xname
    m =MyFinalProperty()
    print m.name
    m.name = "new"
