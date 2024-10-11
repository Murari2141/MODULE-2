def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b
    
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Swapping with a temporary variable...")
a, b = swap_with_temp(a, b)
print("After swapping (with temp): A =", a, ", B =", b)

def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
    
a = int(input("Enter the first number again: "))
b = int(input("Enter the second number again: "))

print("Swapping without a temporary variable...")
a, b = swap_without_temp(a, b)
print("After swapping (without temp): A =", a, ", B =", b)