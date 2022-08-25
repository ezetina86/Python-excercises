"""
    Three exercises working with ranges
    1. Iterate a range  form 0 to 10, and print only numbers module 3
    2. Create a range from 2 to 6 and print them
    3. Create a range from 3 to 10 and increment by 2
"""


def exercise1():
    print("-----")
    print("Exercise 1")
    for number in range(11):
        if number % 3 == 0:
            print(number)


def exercise2():
    print("-----")
    print("Exercise 2")
    for number in range(2, 7):
        print(number)


def exercise3():
    print("-----")
    print("Exercise 3")
    for number in range(3, 11, 2):
        print(number)


# Calling the function exercise1
exercise1()

# Calling the function exercise2
exercise2()

# Calling the function exercise3
exercise3()
