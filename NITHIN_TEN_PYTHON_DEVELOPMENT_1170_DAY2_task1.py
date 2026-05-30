# Enhanced Loan Eligibility System

age = int(input("Enter Age: "))
salary = int(input("Enter Monthly Salary: "))
employment = input("Enter Employment Type (salaried/self-employed): ").lower()

if age < 21 or age > 60:
    print("Rejected: Age must be between 21 and 60.")

elif salary < 25000:
    print("Rejected: Minimum salary requirement is ₹25,000.")

elif employment not in ["salaried", "self-employed"]:
    print("Rejected: Invalid employment type.")

elif 21 <= age <= 30 and salary < 30000:
    print("Needs Guarantor")

elif age > 55 and employment == "self-employed":
    print("High Risk - Senior Review Needed")

else:
    print("Approved")