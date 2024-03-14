# Practical Task 1

# Design a program that determines the award a person competing in a triathlon will receive.
# Follow the pseudocode below to create the program.

"""

Start

- Write code to take in a user's age and store it in an integer variable called age.
- If the user is 40 or over, output the message "You're over the hill.".
- Assume that the oldest someone can be is 100; if the user enters a higher number, output the message "Sorry, you're dead.".
- If the user is 65 or older, output the message "Enjoy your retirement!".
- If the user is under 13, output the message "You qualify for the kiddie
discount.".
- If the user is 21, output the message "Congrats on your 21st!".
- For any other age, output the message "Age is but a number."

- Note that the order in which you set up the conditions is important; you will need to work out what makes sense in terms of the logical tests applied to the ages.

- Reorder the conditions above according to the first block of code where the condition is true and then skip the rest of the conditions:
    1. Assume that the oldest someone can be is 100; if the user enters a higher number, output the message "Sorry, you're dead.".
    2. If the user is 65 or older, output the message "Enjoy your retirement!".
    3. If the user is 40 or over, output the message "You're over the hill.".
    4. If the user is 21, output the message "Congrats on your 21st!".
    5. If the user is under 13, output the message "You qualify for the kiddie
    discount.".
    6. For any other age, output the message "Age is but a number."

End

"""

# Take in a user's age and store it in an integer variable called age.
age = int(input("Please enter your age: "))

# Order and check the conditions according to what makes sense in terms of the logical tests applied to the ages using if-elif-else statements.
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age <= 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")

"""
Successful Test Cases Performed

1. 100
2. 65
3. 40
4. 21
5. 13
6. 33
7. Plus a few other random ones greater than or less than etc.

"""