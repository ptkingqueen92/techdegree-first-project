import random
x = random.randint(1,10)

print("**********Welcome To The Number Guessing Game**********")

guess = int(input("Please pick any number from 1 to 10: "))
num_of_guesses = 1

while guess != x:
        if guess <= 0 or guess > 10:
            print("Please only guess a number from 1 to 10")
            guess = int(input("Please pick any number from 1 to 10: "))
        elif guess < x:
            print("You should guess higher")
            guess = int(input("Please pick any number from 1 to 10: "))
        elif guess > x:
            print("You should guess lower")
            guess = int(input("Please pick any number from 1 to 10: "))
        else:
            break
            
if guess == x:
    print("You guessed it correctly, congratulations!!!")
    print("It took you {} tries to guess the correct number.".format(num_of_guesses))
    try_again = input("Would you like to try again: [yes/no] ")
    while try_again.lower() == 'yes':
        guess = int(input("Please pick any number from 1 to 10: "))
        num_of_guesses = 1

        while guess != x:
            if guess <= 0 or guess > 10:
                print("Please only guess a number from 1 to 10")
                guess = int(input("Please pick any number from 1 to 10: "))
            elif guess < x:
                print("You should guess higher")
                guess = int(input("Please pick any number from 1 to 10: "))
            elif guess > x:
                print("You should guess lower")
                guess = int(input("Please pick any number from 1 to 10: "))
            else:
                break
        if guess == x:
            print("You guessed it correctly, congratulations!!!")
            print("It took you {} tries to guess the correct number.".format(num_of_guesses))
    else:
        print("Thank you for playing this game!")
