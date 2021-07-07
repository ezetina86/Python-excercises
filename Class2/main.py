#Go to game?

print('This program will determine if it is possible to go to the game')
print('Type yes or not...')
vacations = input('Are you on vacations:')
rest_day = input('Are you on your rest_day:')
print(vacations)
print(rest_day)

if (vacations.lower() == 'yes') or (rest_day.lower() == 'yes'):
    print('Congrats! you can go to the game')
else:
    print('Sorry! you cannot go to the game')