def swap_first_two_chars(str1, str2):
    if len(str1) > 1 and len(str2) > 1:
        swapped_str1 = str2[:2] + str1[2:]
        swapped_str2 = str1[:2] + str2[2:]
        return swapped_str1 + " " + swapped_str2
    else:
        return "Strings must be at least 2 characters long."

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = swap_first_two_chars(str1, str2)
print(result)
