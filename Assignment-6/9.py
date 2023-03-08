'''9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.'''

cost=0
quantity=int(input('Enter the quantity: '))
if quantity>=1000:
    cost=quantity-(quantity*0.1)
else:
    cost=quantity*100
print(cost)