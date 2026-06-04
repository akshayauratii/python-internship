temp = float(input("Enter temperature in °C: "))

if temp < 0:
    print("Freezing! Stay indoors and wear heavy clothing")

elif temp >= 0 and temp <= 15:
    print("Cool! A jacket is recommended")

elif temp >= 16 and temp <= 25:
    print("Pleasant weather! Great for outdoor activities")

elif temp >= 26 and temp <= 35:
    print("Hot! Stay hydrated and use sunscreen")

else:
    print("Extreme heat! Avoid going outside")