def insert_string(main_str, insert_str):
    middle_index = len(main_str) // 2
    return main_str[:middle_index] + insert_str + main_str[middle_index:]

main_str = input("Enter the main string: ")
insert_str = input("Enter the string to insert: ")
result = insert_string(main_str, insert_str)
print("Result:", result)
