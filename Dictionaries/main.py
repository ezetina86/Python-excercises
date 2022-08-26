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

# Loop into a dictionary
for key, value in dictionary.items():
    print(key,value)
    
# Loop only keys
for key in dictionary.keys():
    print(key)

# Loop only value
for value in dictionary.values():
    print(value)
    
# Verify if the element exists
print("IDE" in dictionary)

# Adding an element
dictionary["PK"] = "Primary Key"
print(dictionary)

# Is not possible to add duplicate values
dictionary["PK"] = "Primary Key"
print(dictionary)

# Delete an element
dictionary.pop("PK")
print(dictionary)

# Delete all the elements
dictionary.clear()
print(dictionary)

# Delete the dictionary
del dictionary
print(dictionary)
