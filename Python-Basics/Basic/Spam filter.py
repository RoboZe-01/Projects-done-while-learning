# it's a programt to detect spam comments

# step1:give  what is consider to  be spam

s1= "buy this"
s2 = "make a lot of money "
s3 = "subscribe"
s4= "link open"  
 
message = input("Enter your comment : ")
if ((s1 in message)or (s2 in message)or (s3 in message) or (s4 in message)):
    print("this is a spam ")
else :
    print ("this is not a spam")    

 