# EMI Calculator

principal = float(input("Enter Loan Amount: "))
annual_rate = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Loan Duration (Years): "))

monthly_rate = annual_rate / (12 * 100)
months = years * 12

emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
      ((1 + monthly_rate) ** months - 1)

print("\n------ EMI DETAILS ------")
print(f"Loan Amount      : ₹{principal:,.2f}")
print(f"Interest Rate    : {annual_rate}%")
print(f"Duration         : {years} Years")
print(f"Monthly EMI      : ₹{emi:,.2f}")