


# step1: take input from the user for how many rows they want to make this pattern 
# make a input variable

n= int(input ("Enter the number : "))

i = 1
for i in range (1,n+1):
    
    # for space : we have in pattern that space are (n - i)
    # we are using [ end=""] argument which stop cration of new deafault line 


    print(" " * ( n - i ), end="")

   
    # for star : in this pattern start is in odd number ... so we need to multiply it with : [2n*i - 1 ]

    print("😁" * (2*i - 1 ), end="")
    
    print("") #to get new line we use print space




    
    


