"""
    Working with dictionaries
    """

dictionary = {
    "IDE":"Integrated Development Environment",
    "OOP":"Object Oriented Programming",
    "RDBMS":"Relational Database Management System"
}

# Printing a dictionary
print(dictionary)

# Checking the length of a dictionary
print(len(dictionary))

# Accessing into a dictionary
print(dictionary["IDE"])

# Accessing into a dictionary with get
print(dictionary.get('OOP'))

# Modifying elements
dictionary["IDE"]= "integrated development environment"
print(dictionary.get('IDE'))