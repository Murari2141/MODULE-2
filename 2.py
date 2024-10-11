
factorial = 1

num = int(input("Enter Your Number: "))

if num < 0:
    print("Error: Factorial of a negative number doesn't exist")
else:
    for i in range(1, num + 1):
        factorial *= i
    
    print("Factorial of", num, "is", factorial)
