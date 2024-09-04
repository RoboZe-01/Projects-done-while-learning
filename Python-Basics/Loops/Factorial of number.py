

# step1: take input from user

n=int(input("Enter the number : "))

# step2: initialise product variable and apply for loop

product=1
for i in range (1,n+1):

    #step3: use comdition for for loop
    
    
    product= product*i
print(f"Factorial of {n} is { product}")    