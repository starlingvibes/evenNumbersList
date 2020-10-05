#! usr/bin/env python

even_numbers = []


# Function to return the even numbers present in a list
def select_even_numbers(numbers_list):
    for a in numbers_list:
        if a % 2 == 0:
            even_numbers.append(a)
    print(f"The even number(s) present in list is/are: {even_numbers}")


print("\n")


print("""\
\_   _____/__  __ ____   ____    \      \  __ __  _____\_ |__   ___________  ______
 |    __)_\  \/ // __ \ /    \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \/  ___/
 |        \\   /\  ___/|   |  \ /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/\___ \ 
/_______  / \_/  \___  >___|  / \____|__  /____/|__|_|  /___  /\___  >__|  /____  >
        \/           \/     \/          \/            \/    \/     \/           \/ 
""")


print("-------------------------------------------")
try:
    num_list = list(int(num) for num in input("Enter the list numbers separated by space: ").strip().split())

    select_even_numbers(num_list)
except ValueError:
    print("\n")
    print("Oops, that didn't work. Please input numbers in form {int1 int2 intN}")
    print("Without the curly braces of course :-)")
