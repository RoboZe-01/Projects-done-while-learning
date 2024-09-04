


Physics= int(input("Physics marks is :"))
Chemistry = int(input("Chemistry marks are :"))
Maths =     int(input("Maths marks is :"))


# Converting into percentage
total_percentage = ((Physics+Chemistry+Maths)/300)*100

if(total_percentage>40 and Physics>60 and Chemistry>60 and Maths>60):
    print("You are Passed",total_percentage)
else:
    print("You are failed.. Try again next year")
    print("You got :",total_percentage)    