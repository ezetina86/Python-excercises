#age range

age = int(input('Introduce tu edad:'))

twenties = age >= 20 and age <30
thirties = age >= 30 and age <40

if twenties or thirties:
   # print("In range!")
    if twenties:
        print("You're in twenties")
    elif thirties:
        print("You're in thirties")
else:
    print('Not in range!')
