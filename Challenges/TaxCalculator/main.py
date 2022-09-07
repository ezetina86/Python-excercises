# Given a cost the program will calculate the taxes and provide the final cost

def calculate_taxes(price, tax):
    cost_total = 0
    cost_total = (price * (tax/100)) + price
    return cost_total


print('Type the price:')
price = float(input())
print('Type the taxes:')
tax = float(input())

if price > 0:
    if tax > 0:
        print('The total cost is:')
        print(format(calculate_taxes(price, tax), '.2f'))
    else:
        print('Taxes MUST be greater than 0')
else:
    print('Price should be a positive number')
