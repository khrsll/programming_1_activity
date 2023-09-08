# This will be used to generate any random number from 1 to 20.
import random

# The user will have to guess the lucky number generated.
number_to_guess = random.randrange(1,20)

print("Activity in Programming 1\nAlvarez, Lovely Khriselle | EXEC BSIT B16\n")

# This will display the title of the game
# and this will prompt the user that he/she only has five attempts.
print("GUESS THE LUCKY NUMBER\nYou only have five chances to guess the lucky number.\n")

number_of_attempts = 0
max_number_of_attempts = 5

while number_of_attempts < max_number_of_attempts:
    # This will display the first prompt to input any number ranging from 1 to 20.
    # If the guess was incorrect, a different prompt will be displayed
    # to input another number for the next attempt.
    if number_of_attempts == 0:
        guessed_number = int(input("Enter any number ranging from 1 to 20: "))
    else:
        guessed_number = int(input("Choose again: "))
    
    # These prompts will display based on these criteria:
    # - if the lucky number is lower than the guessed number, it will prompt "Ooops! Too low.".
    # - if the lucky number is higher than the guessed number, it will prompt "Ooops! Too high.".
    # - if the user guessed the lucky number, it will display "Congrats! You got it right.",
    #   and it will also display the actual lucky number generated.
    if guessed_number < number_to_guess:
        print("\tOoops! Too low.")
    elif guessed_number > number_to_guess:
        print("\tOoops! Too high.")
    else:
        print("\tCongrats! You got it right.\n")
        print("\tThe lucky number is {}.\n".format(number_to_guess))
        break
    
    number_of_attempts += 1

    # This will calculate the number of attempts left.
    number_of_chances = max_number_of_attempts - number_of_attempts

    # This will display the number of attempts the user has.
    if number_of_chances > 0:
        print("\tYou still have {} chance/s left.\n".format(number_of_chances))
    
# This will display if the user maximizes the number of attempts
# and it will also display the lucky number generated.
if number_of_attempts >= max_number_of_attempts:
    print("\tYou ran out of chances.\n")
    print("\tThe lucky number is {}.\n".format(number_to_guess))

print("Thank you for your participation.")