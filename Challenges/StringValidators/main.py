"""_summary_
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, 
alphanumeric characters, digits, etc.

You are given a string S.

Your task is to find out if the string S contains: 
- alphanumeric characters, 
- alphabetical characters, 
- digits, 
- lowercase and uppercase characters.

https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
"""

from xmlrpc.client import boolean


def hasAlphanumeric(stringInput):
    listInput = [i for i in stringInput]
    listOutput = []
    count = 0
    for element in listInput:
        if element.isalnum():
            count = count + 1
        if count > 0:
            result = True
        else:
            result = False
    return result


def hasAlphabetical(stringInput):
    listInput = [i for i in stringInput]
    listOutput = []
    count = 0
    for element in listInput:
        if element.isalpha():
            count = count + 1
        if count > 0:
            result = True
        else:
            result = False
    return result


def hasDigits(stringInput):
    listInput = [i for i in stringInput]
    listOutput = []
    count = 0
    for element in listInput:
        if element.isdigit():
            count = count + 1
        if count > 0:
            result = True
        else:
            result = False
    return result


def hasLowers(stringInput):
    listInput = [i for i in stringInput]
    listOutput = []
    count = 0
    for element in listInput:
        if element.islower():
            count = count + 1
        if count > 0:
            result = True
        else:
            result = False
    return result


def hasUppers(stringInput):
    listInput = [i for i in stringInput]
    listOutput = []
    count = 0
    for element in listInput:
        if element.isupper():
            count = count + 1
        if count > 0:
            result = True
        else:
            result = False
    return result


if __name__ == '__main__':
    stringInput = input()
    print(hasAlphanumeric(stringInput))
    print(hasAlphabetical(stringInput))
    print(hasDigits(stringInput))
    print(hasLowers(stringInput))
    print(hasUppers(stringInput))
