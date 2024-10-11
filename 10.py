def check_conditions(a, b):
    return a == b or abs(a - b) == 5 or a + b == 5

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = check_conditions(num1, num2)

print(f"Result for {num1} and {num2}: {result}")