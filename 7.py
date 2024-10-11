def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

num = int(input("Enter a number: "))
check_even_odd(num)