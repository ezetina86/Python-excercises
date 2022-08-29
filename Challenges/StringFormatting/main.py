"""_summary_
Given an integer,n , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
"""


from unicodedata import decimal


def convert_decimal(number):
    number = int(number)
    return number


def convert_octal(number):
    return number


def convert_hexadecimal(number):
    return number


def convert_binary(number):
    return number


def print_formatted(number):
    number = int(number)
    for i in range(number):
        print(convert_decimal(i + 1))


if __name__ == '__main__':
    number = input()
    print_formatted(number)
