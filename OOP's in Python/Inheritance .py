

class User : 
    def login(self):
        print(" Login ")

    def register(self):
        print("Registered")    


class Student (User):
    def enroll(self):
        print("Enrolled")


s1 = Student()        
s1.login()            
s1.enroll()
s1.register()
   

# Types of inheritance .. 
#   1. single level : in this only one parent and only one child 
#   2. multilevel : in this child inherot from parents and grandparent and so on 
#   3. Hierarchial in this a parent have multiple children
#   4. multiple : in this a child have to parents  


# Multi level inheritance 


class A :
    def m1(self):
        return 20

class B(A):

    def m1(self):
        return 30
    def m2(self):
        return 40


class C(B):
    def m1(self):
        return 20
    

obj1 = A()
obj2 = B()
obj3 = C()

print(obj1.m1()+obj3.m1() + obj3.m2())







