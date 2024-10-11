def sum_first_n(n):
    return n * (n + 1) // 2

n = int(input("Enter a positive integer: "))

if n > 0:
    result = sum_first_n(n)
    print(f"Sum of first {n} positive integers: {result}")
else:
    print("Please enter a positive integer.")