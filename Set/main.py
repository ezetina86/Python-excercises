"""
    Working with sets
    """

# Creating a set
planets = {'Mars', 'Uranus', 'Earth'}
print(planets)

# Check the length of my set
print(len(planets))

# Verify if a string is in my set
print("Uranus" in planets)
print("Jupyter" in planets)


# Add more elements to this set
planets.add('Jupyter')
print(planets)

# Add the same element
planets.add('Jupyter') # There are no duplicates in sets
print(planets)

# Removing an element of the set
planets.remove("Earth")
print(planets)

# Removing an element of the set using discard
planets.discard("Earth")
print(planets)

# Removing all the elements
planets.clear
print(planets)

# Renove the set
del planets
print(planets) # This will trough an error.


