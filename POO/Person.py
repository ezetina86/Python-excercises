class Person:
    def __init__(self, name, last_name, age):
        # Self is an attribute of the class
        # The right side are parameters
        self.name = name
        self.last_name = last_name
        self.age = age


person1 = Person("Henry", "Zetina", 36)
print(person1.name)
print(person1.last_name)
print(person1.age)

# Creating a second object

person2 = Person('Lili', 'Castro', 37)
print(f'Person 2: {person2.name} {person2.last_name} {person2.age}')
