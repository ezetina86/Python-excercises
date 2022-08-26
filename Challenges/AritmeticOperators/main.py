"""
Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

"""


def sum(a, b):
    result = a + b
    return result


def test_sum():
    assert sum(a, b) == 2
    #print("Function sum is working as expected ...")
    return True


def difference(a, b):
    result = a - b
    return result


def test_difference():
    assert difference(1, 1) == 0
    #print("Function difference is working as expected ...")
    return True


def product(a, b):
    result = a * b
    return result


def test_product():
    assert product(1, 1) == 1
    #print("Function product is working as expected ...")
    return True


if __name__ == '__main__':
    # Verify that the functions are working
    if test_sum():
        pass
    elif test_difference():
        pass
    elif test_product():
        pass
    else:
        print("Error, check your code!")

    print("Ingress two numbers and I'm going to calculate the  sum, difference, and product of them...")
    print("Ingress first number:")
    a = int(input())
    print("Ingress second number:")
    b = int(input())
    print("The sum of the numbers is:")
    print(sum(a, b))
    print("The difference of the numbers is:")
    print(difference(a, b))
    print("The product of the numbers is:")
    print(product(a, b))
