def add_suffix(input_str):
    if len(input_str) >= 3:
        suffix = 'ly' if input_str.endswith('ing') else 'ing'
        return input_str + suffix
    else:
        return input_str

input_str = input("Enter a string: ")
result = add_suffix(input_str)
print(result)
