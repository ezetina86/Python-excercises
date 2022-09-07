# Print numbers 5 to 1 using a recursive function

def printReverse(num):
    if num == 0:
        return
    else:
        print(num)
        printReverse(num-1)


print('Ingress a number:')
num = int(input())
if num >= 0:
    print("----")
    printReverse(num)
else:
    print('Only positive numbers allowed!')
