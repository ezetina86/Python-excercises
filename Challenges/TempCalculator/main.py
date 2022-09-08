"""_summary_
Create a program to convert Celsius to Fahrenheit and viceversa
"""


def celsius_to_fahrenheit(temperature):
    conversion = float(((temperature * (9/5)) + 32))
    return conversion


def fahrenheit_to_celsius(temperature):
    conversion = float((temperature-32) * (5/9))
    return conversion


def select_option():
    print('To convert Celsius to Fahrenheit select 1')
    print('To convert Fahrenheit to Celsius select 2')
    option = 0
    temperature = 0
    result = 0
    option = int(input())
    if option == 1:
        print('Celsius to Fahrenheit selected')
        print('Ingress the Celsius grades:')
        temperature = float(input())
        result = celsius_to_fahrenheit(temperature)
        print(f'{temperature} grades Celsius are {result} grades Fahrenheit')
    elif option == 2:
        print('Fahrenheit to Celsius selected')
        print('Ingress the Fahrenheit grades:')
        temperature = float(input())
        result = fahrenheit_to_celsius(temperature)
        print(f'{temperature} grades Fahrenheit are {result} grades Celsius')
    else:
        print('Invalid option...')
        select_option()


if __name__ == "__main__":
    print('Welcome to the temperature calculator, please select an option')
    select_option()
