"""_summary_
Tuples exercises
    """

# Create a list that includes only numbers less than 5
aTuple = (13, 1, 8, 3, 2, 5, 8)
# Define a list
aList = []

# Filer numbers less than 5 
for element in aTuple:
    if element < 5:
        aList.append(element)

print(aList)
