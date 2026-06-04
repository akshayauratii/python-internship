import math

def calculate_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12

    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    return emi

principal = float(input("Enter Loan Amount: "))
rate = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Loan Tenure (Years): "))

emi = calculate_emi(principal, rate, years)

print(f"\nMonthly EMI: ₹{emi:.2f}")