# Logic Operators
a = True
b = False

result = a and b
print(result)
result = a or b
print(result)


####
value = int(input('type the valuie: '))
min = 0
max = 5
range = (value >= min) and (value <= max)
if range:
    print(f'your value {value} is in range')
else:
    print(f'your value {value} is not in range')
