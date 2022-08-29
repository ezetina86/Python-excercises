# Define a function
def my_function():
    print("Hello World!")


my_function()
# It's possible to call a function multiple times
my_function()


def new_function(name, last_name):
    print('Hello!', f'{name}', f'{last_name}')


new_function('Henry', 'Zetina')
new_function('Henry', 'Moya')


def sum(a, b):
    a = int(a)
    b = int(b)
    return (a + b)


print('Give me 2 numbers')
a = input()
b = input()
# print(type(a))
result = sum(a, b)
print(f'Result of the sum: {result}')
