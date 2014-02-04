class MySingleton(object):
    _instance=None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MySingleton,cls).__new__(cls)
        return cls._instance           
            
s1=MySingleton()
s2=MySingleton()
if(id(s1)==id(s2)):
    print "Same"
else:
    print "Different"