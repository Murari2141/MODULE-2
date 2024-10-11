def get_first_last_2_chars(input_str):
    if len(input_str) < 2:
        return "Instead"
    elif len(input_str) == 2:
        return input_str * 2
    else:
        return input_str[:2] + input_str[-2:]

input_str = input("Enter a string: ")
result = get_first_last_2_chars(input_str)
print("Result:", result)
