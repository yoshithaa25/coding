'''delete method
#syntax __del__()
class abc():
    classvar=0
    def __init__(self,var):
        abc.classvar +=1
        self.var=var
        print("the object value:",var)
        print("the class var value:",abc.classvar)
    def __del__(self):
        abc.classvar -=1
        print("object with value %d is going outof scope" %self.var)
obj1=abc(10)
obj2=abc(20)
obj3=abc(30)
del obj1
del obj2'''

'''special methods
__rper__() 
__len__() #len of srtring
__cmp__() #compare 2 objects
__call__()
__hash__() #it will decide where the obj is placed in data structure

OPERATIONAL
__gt__(),_ge__(),__lt__(),__eq__(),__ne__() #methods to compare 2 obj in class
__iter__()
__getitem__() #it will get a empty location with a space
__setitem__() #used to assign a value to a space

class num():
    def __init___(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
numlist=num([1,2,3,4,5,6,7,8,9])
print("before modify")
print(numlist.mylist)
numlist[3]=10
print("after modify")
print(numlist.mylist)

#print variable and private variables
class abc():
    def __init__(self,v1,v2):
        self.v1=v1  #public var
        self.__v2=v2   #private var
    def display(self):
        print("from class method:",self.v1)
        print("from class method:",self.__v2)
obj=abc(10,100)
obj.display()
print("from main module:var1=",obj.v1)
print("from main module:var1=",obj.__v2)

#built in class attributes __dict__,__doc__,__name__,__module__,___bases__
class abc():
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
    def display(self):
        print("var1:",self.v1)
        print("var2:",self.v2)
obj=abc(11,1.2345)
print("object.__dict__=",obj.__dict__)
print("object.__doc__=",obj.__doc__)
print("class.__name__=",abc.__name__)
print("object.__module=",obj.__module__)
print("class.__bases__=",abc.__bases__)'''

#inheritance-multiple
#code to demonstrate the call from super class through constructor of base class
class base1(object):
    def __init__(self):
        print("base class-1")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("base class-2")
        super(base2,self).__init__()
class derived(base1,base2):
    def __init__(self):
        super(derived,self).__init__()
        print("derived-class")
d=derived()        










        



