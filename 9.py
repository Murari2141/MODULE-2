def sum_three_numbers(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

result = sum_three_numbers(num1, num2, num3)

print("Sum of:", result)