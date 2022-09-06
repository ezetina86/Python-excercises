# Recursive function

def factorial(num):
    if num == 1:
        return 1
    else:
        # Calling the function itself
        return num * factorial(num-1)


result = factorial(1)
print(f'The factorial of 5 is {result}')
