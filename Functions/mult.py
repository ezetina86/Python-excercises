def multiplyValues(*args):
    result = 1
    for element in args:
        result = element * result
    print(result)


print(multiplyValues(3, 5, 15, 3))
