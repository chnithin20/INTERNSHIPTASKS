# Production Counter System

target = int(input("Enter Production Target: "))

produced = 0
defects = 0

for shift in range(1, 4):  # 3 shifts

    print(f"\nShift {shift} Started")

    for machine in range(1, 21):  # 20 machines

        # Example defect rule
        if machine % 7 == 0:
            defects += 1
            print(f"Machine {machine}: Defective Item")
            continue

        produced += 1
        print(f"Machine {machine}: Produced Item")

        if produced >= target:
            print("\nTarget Achieved!")
            break

    if produced >= target:
        break

total_attempts = produced + defects

if total_attempts > 0:
    productivity = (produced / total_attempts) * 100
else:
    productivity = 0

print("\n===== PRODUCTION REPORT =====")
print("Items Produced :", produced)
print("Defective Items:", defects)
print("Productivity   :", round(productivity, 2), "%")