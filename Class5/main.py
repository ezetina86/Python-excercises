"""_summary_
Working with lists in Python
"""
# Defining a list of names

from cmath import pi
from operator import le

names = ["John", "Henry", "Richard", "Lili"]

# Printing the names list

print(names)

# Printing a value fo my list
print(names[0])

# Printing a value of my list in reverse
print(names[-1])

# Print ranges from a list, it prints 0 an 1 values
print(names[0:2])

# Print from start without including the first element
print(names[:3])

# Print list until end
print(names[1:])

#Change valued from list
names[1] = "Bobby"
print(names)

# Iterate a list
for name in names:
    print(name)
else:
    print("No more names!")
    
# How length is my list?
print(len(names))

# Adding elements to my list

names.append("Henry")
print(names)

# Adding elements to my list into an specific index
names.insert(1,"Mike")
print(names[1])
print(names)

# Delete an element
names.remove("Lili")
print(names)

# Delete the last element
names.pop()
print(names)

# Delete an specific index
del names[0]
print(names)

# Clean the list
names.clear()
print(names)

# Delete the list
del names
# This will return an error since the list doesn't exists anymore
print(names)

