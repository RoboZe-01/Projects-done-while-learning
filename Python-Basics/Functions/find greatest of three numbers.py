
# step 1 :initialise variables
a = 1
b = 2 
c =  8

# step2: define the function 

def greatest_number(a,b,c):

    if (a>b and a>c ):
        print(a,"is the largest of three")
        return a
    elif( b>a and b>c):
        print(b, "is the largest number")
        return b
    else:
        print(c,"is the largest number")
        return c  


a=32
b=43
c=56

print(greatest_number(a,b,c))











