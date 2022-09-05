"""_summary_
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
For example, alison heck should be capitalized correctly as Alison Heck."""


def solve(s):
    return s.title()


if __name__ == '__main__':
    s = input("Enter a String: \n")
    print(solve(s))
