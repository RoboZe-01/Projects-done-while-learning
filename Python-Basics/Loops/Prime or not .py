# Input the number to check
num = int(input("Enter a number: "))

# Check if the number is prime
if num <= 1:
    is_prime = False
else:
    is_prime = True
    i = 2
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

# Output the result
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
