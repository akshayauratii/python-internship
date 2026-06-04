# 1. Inputs: total bill amount, number of people, and tip percentage
total_bill = float(input("Enter the total bill amount ($): "))
number_of_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

# 2. & 3. Calculations using all mandatory arithmetic operators (+, -, *, /, %)

# [*] Multiplication: Calculate the raw tip amount
tip_amount = total_bill * (tip_percentage / 100)

# [+] Addition: Calculate total bill including the tip
total_with_tip = total_bill + tip_amount

# [/] Division: Calculate the base amount per person
amount_per_person = total_with_tip / number_of_people

# [%] Modulo: Calculate if there's any leftover remainder from an uneven split cents-wise
remainder = total_with_tip % number_of_people

# [-] Subtraction: Just to fulfill the mandatory '-' operator requirement,
# let's show how much of the final total was strictly due to the extras (total minus original bill)
total_extra_costs = total_with_tip - total_bill

# 4. Round results to 2 decimal places using round() and print a neat summary
rounded_tip = round(tip_amount, 2)
rounded_total = round(total_with_tip, 2)
rounded_per_person = round(amount_per_person, 2)
rounded_remainder = round(remainder, 2)

print("\n" + "_"*35)
print("          BILL SPLIT SUMMARY")
print("_"*35)
print(f"Initial Bill:       ${total_bill:.2f}")
print(f"Tip Added ({tip_percentage}%): ${rounded_tip:.2f}")
print(f"Total Extra Costs:  ${total_extra_costs:.2f}")
print(f"Grand Total:        ${rounded_total:.2f}")
print(f"Number of People:   {number_of_people}")
print("-"*35)
print(f"AMOUNT PER PERSON:  ${rounded_per_person:.2f}")
print(f"Uneven Remainder:   ${rounded_remainder:.2f}")
print("_"*35)