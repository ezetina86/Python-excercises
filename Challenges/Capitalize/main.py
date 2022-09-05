"""_summary_
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
For example, alison heck should be capitalized correctly as Alison Heck."""


def solve(s):
    capitalized_string = ""
    the_string = s.split()
    print(the_string)
    listOutput = []
    for word in the_string:
        word = word.capitalize()
        print(word)
        listOutput.append(word)
        print(listOutput)
    capitalized_string = ' '.join(listOutput)
    print(capitalized_string)
    return capitalized_string


if __name__ == '__main__':
    s = input("Enter a String: \n")
    solve(s)
