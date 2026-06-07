# question 1
def perform_division():
    try:
        # Prompt user for numerator and denominator
        numerator = float(input("Enter the first number (numerator): "))
        denominator = float(input("Enter the second number (denominator): "))
        
        # Calculate result
        result = numerator / denominator
        print(f"The result of division is: {result}")
        
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")
    except ValueError:
        print("Error: Invalid numeric input. Please enter numbers only.")

if __name__ == "__main__":
    perform_division()

    