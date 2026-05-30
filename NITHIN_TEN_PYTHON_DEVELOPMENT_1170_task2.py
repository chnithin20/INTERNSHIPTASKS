bill = float(input("Enter total bill amount: ₹"))
people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))
tip_amount = (bill * tip_percent) / 100
total_bill = bill + tip_amount
per_person = total_bill / people
remaining = int(total_bill) % people
print("\n===== BILL SUMMARY =====")
print(f"Original Bill     : ₹{bill:.2f}")
print(f"Tip Amount        : ₹{tip_amount:.2f}")
print(f"Total with Tip    : ₹{total_bill:.2f}")
print(f"Amount Per Person : ₹{round(per_person, 2)}")
print(f"Remainder (mod %) : {remaining}")
print("========================")