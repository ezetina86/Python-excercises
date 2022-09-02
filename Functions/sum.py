"""_summary_
Create a function to sum values received, it is needed to use *args as parameters in the function
and return  the result of the sum of all the arguments
"""
# Defining the function


def sumValues(*args):
    result = 0
    # Iterate each argument
    for element in args:
        result += element
    print(result)


# Calling the function
print(sumValues(3, 5, 9, 4, 6))
