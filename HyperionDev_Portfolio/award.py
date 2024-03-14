# Practical Task 1

# Design a program that determines the award a person competing in a triathlon will receive.
# Follow the pseudocode below to create the program.

"""

Start

- Your program should read in the times (in minutes) for all three events of a triathlon, namely swimming, cycling, and running.
- Then calculate and display the total time taken to complete the triathlon.
- The award a participant receives is based on the total time taken to complete the triathlon.
- The qualifying time for awards is 100 minutes.
- Display the award that the participant will receive based on the following criteria:

- Qualifying Criteria
1. Within the qualifying time.
2. Within 5 minutes of the qualifying time.
3. Within 10 minutes of the qualifying time.
4. More than 10 minutes off from the qualifying time.

- Time Range
1. 0 - 100 minutes
2. 101 - 105 minutes
3. 106 - 110 minutes
4. 111+ minutes

- Award
1. Provincial Colours
2. Provincial Half Colours
3. Provincial Scroll
4. No award

End

"""

# Take in the times for swimming, cycling and running.
swimming_time = int(input("Enter swimming time (in minutes): "))
cycling_time = int(input("Enter cycling time (in minutes): "))
running_time = int(input("Enter running time (in minutes): "))

# Calculate and display the total time taken to complete the triathlon.
total_time = swimming_time + cycling_time + running_time
print(f"Total time taken: {total_time} minutes")

# Determine the award based on the total time.
if total_time <= 100:
    award = "Provincial Colours"
elif total_time <= 105:
    award = "Provincial Half Colours"
elif total_time <= 110:
    award = "Provincial Scroll"
else:
    award = "No award"

# Display the award that the participant will receive.
print(f"Award: {award}")

# Successful test cases performed for each and used 'run and debug' to check everything executed properly! :-)
