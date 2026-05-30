name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))
city = input("Enter your city: ").strip()
favourite_subject = input("Enter your favourite subject: ").strip()

birth_year = 2024 - age

print("\n" + "=" * 40)
print("        PERSONAL PROFILE CARD")
print("=" * 40)
print(f"Name             : {name}")
print(f"Age              : {age}")
print(f"City             : {city}")
print(f"Favourite Subject: {favourite_subject}")
print(f"Birth Year       : {birth_year}")
print("=" * 40)