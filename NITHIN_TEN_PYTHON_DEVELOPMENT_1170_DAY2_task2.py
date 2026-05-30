# Smart Temperature Advisor

temp = float(input("Enter Temperature (°C): "))

if temp < 0:
    print("Freezing! Stay indoors and wear heavy clothing.")

elif 0 <= temp <= 15:
    print("Cold. A jacket is recommended.")

elif 16 <= temp <= 25:
    print("Pleasant weather! Great for outdoor activities.")

elif 26 <= temp <= 35:
    print("Hot. Stay hydrated and use sunscreen.")

else:
    print("Extreme heat! Avoid going outside.")