
class Fraction :
    
    
    
    def __init__(self,n,d) :

        self.num= n
        self.den = d
    

        # here we defined how our datatype will look 

    def __str__(self) :
        return "{}/{}".format(self.num,self.den)
    
    


      # Here we will show how to make addintion method in our datatype


    def __add__(self,other):

        temp_num = self.num*other.den + other.num*self.den
        temp_den = self.den * other.den  
        return "{}/{}".format(temp_num,temp_den)
    
       # defining how to substract the datatype

    def __sub__(self,other):

        temp_num = self.num*other.den - other.num*self.den
        temp_den = self.den * other.den  
        return "{}/{}".format(temp_num,temp_den)    
    
    
    def __mul__(self,other):

        temp_num = self.num* other.num
        temp_den = self.den * other.den  
        return "{}/{}".format(temp_num,temp_den)    


    def __truediv__(self,other):

        temp_num = self.num* other.den
        temp_den = self.den * other.num  
        return "{}/{}".format(temp_num,temp_den)    

x = Fraction(5,6)        
y=Fraction(4,8)
print(x) 
print(y)   
print(x+y)
print(x-y) 
print(x*y)
print(x/y)