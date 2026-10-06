class Test:
    def __init__(self,name,age):
        print("My Name is=",name)
        print("My age is=",age)
t1=Test("Kiran",21)

class Test:
    def __init__(self,name):
        self.name=name
        
t1=Test("Kiran")
print(t1)

class Student:
    inst_name="FullStack  Expert Academy"
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def displayDetails(self):
        print("My name is :",self.name)
        print("My age is :",self.age)
        print("My course is :",self.course)
        print("Institute Name :",Student.inst_name)
s1=Student("Kiran",21,"python")
s1.displayDetails()
class Student:
    def __init__(self):
        print("Object is created: Constructor is invoked")
    def __del__(self):
        print("Object is going to be destroyed: Destructor is invoked")
s1=Student()
print("We gonna delete the object")
del s1
print("Program Ended")
class Test:
    @classmethod
    def m1(cls):
        print("This is class method")
Test.m1()
class Student:
    institute="Fullstack"
    
    def m2(self):
        self.name="Hero"
        print("Static Method",self.institute)
        print("Instance Method",self.name)
    @classmethod
    def m1(cls):
        print("Static Method",cls.institute)
        print("Instance Method",cls.name)
s1=Student()
s1.m2()
Student.m1()