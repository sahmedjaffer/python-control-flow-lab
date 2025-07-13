# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

from calendar import month


def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()




# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input('Enter a letter: ')
    if letter in 'aeiou' or letter in 'AEIOU':
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")
# Call the function
check_letter()



# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here

    age = int(input("Please enter your age: "))
    if age > 0:
        voting_age = 18
        if age >= voting_age:
            print("You are eligible to vote.")
        else:
            print("Sorry, you are not eligible to vote yet.")
    else:
        print("Invalid age entered. Please enter a positive number.")


# Call the function
check_voting_eligibility()



# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_age = int(input("Input a dog's age: "))
    if dog_age > 0:
        if dog_age <= 2:
            dog_age_in_dog_years = dog_age * 10
            print(f"The dog's age in dog years is {dog_age_in_dog_years}.")
        elif dog_age > 2:
            dog_age_in_dog_years = 20 + (dog_age - 2) * 7
            print(f"The dog's age in dog years is {dog_age_in_dog_years}.")
    else:
        print("Invalid age entered. Please enter a positive number.")

# Call the function
calculate_dog_years()



# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here

    is_cold = input('Is it cold? (yes/no): ').lower()
    is_raining = input('Is it raining? (yes/no): ').lower()

    if is_cold == 'yes' and is_raining == 'yes':
        print("Wear a waterproof coat.")
    elif is_cold == 'yes' and not is_raining == 'yes':
        print("Wear a warm coat.")
    elif not is_cold == 'yes' and is_raining == 'yes':
        print("Carry an umbrella.")
    elif not is_cold == 'yes' and not is_raining == 'yes':
        print("Wear light clothing.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Call the function
weather_advice()



# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    month_days = {
        'JAN': 31, 'FEB': 29, 'MAR': 31, 'APR': 30, 'MAY': 31, 'JUN': 30,
        'JUL': 31, 'AUG': 31, 'SEP': 30, 'OCT': 31, 'NOV': 30, 'DEC': 31
    }

    month = input('Enter the month of the year (Jan - Dec): ').upper()
    if month not in month_days:
        print("Invalid month. Please enter a valid three-letter month abbreviation.")
        return
    
    day = input('Enter the day of the month: ')
    if day.isdigit() == False :
        print("Invalid day. Please enter a numeric value for the day.")
        return
    else:
        day = int(day)
        if day < 1 or day > month_days[month]:
            print("Invalid day. Please enter a valid day for the given month.")
            return

    if (month == 'DEC' and day >= 21) or month == 'JAN' or month == 'FEB' or (month == 'MAR' and day < 20):
        print(f"{month} {day} is in Winter.")
    elif (month == 'MAR' and day >= 20) or month == 'APR' or month == 'MAY' or (month == 'JUN' and day < 21):
        print(f"{month} {day} is in Spring.")
    elif (month == 'JUN' and day >= 21) or month == 'JUL' or month == 'AUG' or (month == 'SEP' and day < 22):
        print(f"{month} {day} is in Summer.")
    elif (month == 'SEP' and day >= 22) or month == 'OCT' or month == 'NOV' or (month == 'DEC' and day < 21):
        print(f"{month} {day} is in Fall.")
    else:
        print("Invalid month or day")

  

# Call the function
determine_season()


  

# Call the function
determine_season()



# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here

    number = 50
    for attempts in range(1, 6):
            guess = int(input(f'Attempt No. {attempts}: Guess a number between 1 and 100: '))
            if guess == number:
                print("Congratulations, you guessed correctly!")
                break
            elif guess < number-10:
                print("Guess is too low.")
            elif guess < number:
                print("Guess is slightly low.")
            elif guess > number:
                print("Guess is slightly high.")
            elif guess > number+10:
                print("Guess is too high.")
            if attempts == 5:
                print("Sorry, you failed to guess the number in five attempts.")

# Call the function
guess_number()

