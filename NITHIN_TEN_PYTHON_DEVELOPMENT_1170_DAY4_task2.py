# Tax Calculator

income = float(input("Enter Annual Income: "))

if income <= 250000:
    tax = 0

elif income <= 500000:
    tax = (income - 250000) * 0.05

elif income <= 1000000:
    tax = 12500 + (income - 500000) * 0.20

else:
    tax = 112500 + (income - 1000000) * 0.30

print("\n------ TAX REPORT ------")
print(f"Annual Income : ₹{income:,.2f}")
print(f"Tax Payable   : ₹{tax:,.2f}")
print(f"Net Income    : ₹{income-tax:,.2f}")