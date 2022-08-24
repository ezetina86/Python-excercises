#for i in range(6):
#    #Print only even numbers
#    if i % 2 ==0:
#        print(f'Value:{i}')
        
for i in range (6):
    #Print only even numbers skipping odds
    if i % 2 != 0:
        # The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.
        continue
    print(f'Value:{i}')
