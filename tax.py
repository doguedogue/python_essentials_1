income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Write the rest of your code here.
else:
    tax = 14839.2 + round(income - 85528, 0) * 0.32

tax = round(tax, 0)
if tax < 0: 
    tax = 0
print("The tax is:", tax, "thalers")