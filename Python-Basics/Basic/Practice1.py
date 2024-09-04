a=int(input("Enter first number:"))
b=int(input("Enter Second number"))
c=int(input("Enter Third number:"))
d=int(input("Enter Fourth number"))




if a>b and a>c and a>d:
    print("a is the highest number",a)
elif b>a and b>c and b>d:
    print("b is the highest number",b)    
elif c>a and c>b and c>d:
    print("highest number is c:",c)
else:
    print("d is the highest number",d)        