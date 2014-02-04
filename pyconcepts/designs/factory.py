

class A(object):
    def data(self):
        print "A"

class B(object):
    def data(self):
        print "B"

class C(object):
    @classmethod
    def check(cls,data):
        return cls().data(data)
            
    def data(self,type):        
        if type=='A':
            obj=A()
        if type=='B':
            obj=B()
        return obj.data()
    
class D(C):
    pass

D().check("A")
D().check("B")
