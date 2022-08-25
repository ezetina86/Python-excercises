"""_summary_
Working with tuples, which is a immutable data type
    """
# Creating a  tuple
fruits = ('Orange', 'Banana', 'Dragon fruit')
print(fruits)

# Length of a tuple
print(len(fruits))

# Accessing one element of the tuple
print(fruits[0])
print(fruits[-1])
# Not including the last element
print(fruits[0:-1])

# Loops and tuples
for fruit in fruits:
    print(fruit, end=' ')
    
# A tuple is immutable
# fruits[0] = 'Pineapple'
fruitsList = list(fruits)
fruitsList [0] = 'Pineapple'
print('\n',fruitsList)
fruits = tuple(fruitsList)
print('\n',fruits)