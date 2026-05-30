# Attendance Calculator

attended = int(input("Enter Classes Attended: "))
total = int(input("Enter Total Classes Conducted: "))

attendance = (attended / total) * 100

print("\n------ ATTENDANCE REPORT ------")
print(f"Attendance Percentage : {attendance:.2f}%")

required = 75

if attendance >= required:
    print("Eligible for Exams")
else:
    needed = 0

    while ((attended + needed) / (total + needed)) * 100 < required:
        needed += 1

    print("Not Eligible")
    print(f"Attend at least {needed} more classes to reach 75%")