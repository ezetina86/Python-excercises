# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM

def swap_case(stringInput):
    '''Takes an input and swap lowercase letters to uppercase letters'''
    # Check if variable is string
    stringOutput = stringInput
    if isinstance(stringInput, str):
        # Swapping cases
        stringOutput = stringOutput.swapcase()
    else:
        print("ERROR: the input MUST be a string")
    return stringOutput

# New function using a list instead fo a prebuilt function to swap cases


def swap_case2(stringInput):
    '''Takes an input and swap lowercase letters to uppercase letters using a list'''
    # Converting a list into a string
    listInput = [i for i in stringInput]
    listOutput = []
    stringOutput = ""
    for element in listInput:
        if element.isupper():
            # String is immutable, so it's needed to re-assign the value with the swapcase
            element = element.lower()
            listOutput.append(element)
        else:
            element = element.upper()
            listOutput.append(element)

    for element in listOutput:
        # Adding each element of the list into a string
        stringOutput += element

    return stringOutput


def test_swap_case():
    assert swap_case("a") == "A"
    print("Function swap_case is working as expected ...")


def test_swap_case2():
    assert swap_case2("Bb") == "bB"
    print("Function swap_case2 is working as expected ...")


if __name__ == '__main__':
    print("Unit Test for functions created ...")
    test_swap_case()
    print("Test 1 passed ...")
    test_swap_case2()
    print("Test 2 passed ...")
    print("Insert a string I'm going to swap the cases!")
    stringInput = input()
    result = swap_case(stringInput)
    result2 = swap_case(stringInput)
    print(result)
    print(result2)
