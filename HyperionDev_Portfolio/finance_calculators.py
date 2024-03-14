# 1st Capstone Project: Financial Calculator

# Users of this programme have access to two financial calculators:
# 1. To calculate the amount of interest they'll earn on their investment.
# 2. To calculate the amount they'll have to repay on a home loan each month.

# Previous tasks feedback notes to bear in mind
# 1. Try keeping line width to a max of 80 characters
    # This was difficult to do with the formulas
# 2. Incorporate error handling for user inputs
    # This is probably the main reason I took so long to do this task
    # I spent time looking online and tried various loop variations
    # It took me much longer than expected but I'm quite happy with the final result! :-)
    # And I learned a lot throughout the process!

# PS: I tried to make it as user friendly as possible!


# Import the math module
import math

# Display the menu to the user
print("\ninvestment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# Prompt the user to enter the calculation type and convert the input to lowercase
# Use a while loop with and if-else statement to keep checking for the correct user input
while True:
    calculation_type = input("\nPlease enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Check if the user entered a valid choice, then exit the loop if the input is valid
# Use a list for easy retrieval and potential alterations such as adding a 'savings' option
    if calculation_type in ['investment', 'bond']:
        break
    # If the user doesn't type in a valid input, show an appropriate error message
    else:
        print("\nInvalid choice.")

# If the user chooses 'investment', proceed with the following
if calculation_type == "investment":
    print("\nYou selected investment.\n")

# Prompt the user to enter the deposit amount
# Use a while loop + try-except to check for correct user input and handle any errors
    while True:
        try:
            deposit = float(input("Please enter the amount of money you are depositing: "))
            break
        # If the user doesn't type in a valid input, show an appropriate error message
        except ValueError:
            print("\nInvalid input.\n")

# Prompt the user to enter the interest rate percentage
# Use a while loop + try-except to check for correct user input and handle any errors
    while True:
        try:
            interest_rate = float(input("\nPlease enter the interest rate percentage (as a number only e.g. 1, 2, 3 etc.): ")) / 100
            break
        # If the user doesn't type in a valid input, show an appropriate error message
        except ValueError:
            print("\nInvalid input.")

# Prompt the user to enter the number of years for the investment
# Use a while loop + try-except to check for correct user input and handle any errors
    while True:
        try:
            num_years = int(input("\nPlease enter the number of years you plan on investing for: "))
            break
        # If the user doesn't type in a valid input, show an appropriate error message
        except ValueError:
            print("\nInvalid input.")

# Prompt the user to choose between simple or compound interest and convert the input to lowercase
# Use a while loop + try-except to check for correct user input and handle any errors
    while True:
        interest = input("\nPlease choose either 'simple' or 'compound' interest: ").lower()

        if interest in ['simple', 'compound']:
            break
        # If the user doesn't type in a valid input, show an appropriate error message
        else:
            print("\nInvalid choice.")

    # If the user chooses simple interest
        # Calculate the total investment using the simple interest formula
    if interest == "simple":
        total_investment = round(deposit * (1 + interest_rate * num_years), 2)
        # Display the total investment amount
        print(f"\nThank you. Your total investment will amount to £{total_investment:.2f}.")

    # If the user chooses compound interest
        # Calculate the total investment using the compound interest formula
    elif interest == "compound":
        total_investment = round(deposit * math.pow((1 + interest_rate), num_years), 2)
        
        # Display the total investment amount
        print(f"\nThank you. Your total investment will amount to £{total_investment:.2f}.")

# If the user chooses 'bond', proceed with the following
elif calculation_type == 'bond':
    print("\nYou selected bond.")

# Prompt the user to enter the value of the house
# Use a while loop + try-except to check for correct user input and handle any errors
    while True:
        try:
            house_value = float(input("\nPlease enter the present value of the house: "))
            break
        # If the user doesn't type in a valid input, show an appropriate error message
        except ValueError:
            print("\nInvalid input.")

# Prompt the user to enter the interest rate percentage
# Use a while loop + try-except to check for correct user input and handle any errors
    while True:
        try:
            interest_rate = float(input("\nPlease enter the interest rate percentage (as a number only e.g. 1, 2, 3 etc.): "))
            break
        # If the user doesn't type in a valid input, show an appropriate error message
        except ValueError:
            print("\nInvalid input.")

# Prompt the user to enter the number of years they plan on taking to repay the bond
# Use a while loop + try-except to check for correct user input and handle any errors
    while True:
        try:
            num_months = int(input("\nPlease enter the number of months you plan on taking to repay the bond: "))
            break
        # If the user doesn't type in a valid input, show an appropriate error message
        except ValueError:
            print("\nInvalid input.")

    # Calculate and display the monthly repayments amount
    monthly_repayments = round(((interest_rate / 100 / 12) * house_value) / (1 - math.pow(1 + interest_rate / 100 / 12, -num_months)), 2)
    print(f"\nYour monthly repayment amount will be £{monthly_repayments:.2f}.")
