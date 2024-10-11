def reverse_str_if_mul_of_4(input_str):
    if len(input_str) % 4 == 0:
        return input_str[::-1]
    else:
        return input_str

input_str = input("Enter a string: ")
result = reverse_str_if_mul_of_4(input_str)
print("Result:", result)
