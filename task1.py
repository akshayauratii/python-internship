# 1. Ask the user for their information
name = input("Enter your name: ")
age_str = input("Enter your age: ")
city = input("Enter your city: ")
favourite_subject = input("Enter your favourite subject: ")

# Convert age to an integer to perform calculations
age = int(age_str)

# 2. & 3. Calculate birth year (as per the prompt instruction: 2024 - age)
birth_year = 2024 - age

# 4. Display a formatted profile card using print() and f-strings
print("\n" + "="*30)
print(f"      PERSONAL PROFILE CARD")
print("="*30)
print(f"Name:              {name}")
print(f"Age:               {age}")
print(f"Estimated Birth:   {birth_year}")
print(f"City:              {city}")
print(f"Favourite Subject: {favourite_subject}")
print("="*30)
