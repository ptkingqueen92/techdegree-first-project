import random
x = random.randint(1,10)


print("**********Welcome To The Number Guessing Game**********")


def get_valid_guess():
    while True:
        guess = input("Enter any number from 1 to 10: ")
        num_of_guesses = 1
        try:
            guess = int(guess)
            return guess
        except:
            print("Not an integer, try again!")
            continue

guess = get_valid_guess()
user_guess = int(input("Enter any number from 1 to 10: "))


while guess != x:
        if guess <= 0 or guess > 10:
            print("Guess a number from 1 to 10")
            user_guess = int(input("Enter any number from 1 to 10: "))
            num_of_guesses += 1
        elif guess < x:
            print("You should guess higher")
            user_guess = int(input("Enter any number from 1 to 10: "))
            num_of_guesses += 1
        elif guess > x:
            print("You should guess lower")
            user_guess = int(input("Enter any number from 1 to 10: "))
            num_of_guesses += 1
        else:
            break
            
if guess == x:
    print("You guessed it correctly, congratulations!!!")
    print("It took you {} tries to guess the correct number.".format(num_of_guesses))
    num_of_guesses += 1


try_again = "yes"
try_again = input("Would you like to try again: [yes/no] ")

while try_again == 'yes':
        x = random.randint(1,10)
        user_guess = int(input("Please pick any number from 1 to 10: "))
        num_of_guesses = 1
        while guess != x:
                if guess <= 0 or guess > 10:
                        print("Please only guess a number from 1 to 10")
                        user_guess = int(input("Please pick any number from 1 to 10: "))
                        num_of_guesses += 1
                elif guess < x:
                        print("You should guess higher")
                        user_guess = int(input("Please pick any number from 1 to 10: "))
                        num_of_guesses += 1
                elif guess > x:
                        print("You should guess lower")
                        user_guess = int(input("Please pick any number from 1 to 10: "))
                        num_of_guesses += 1
                else:
                        break

        if guess == x:
                print("You guessed it correctly, congratulations!!!")
                print("It took you {} tries to guess the correct number.".format(num_of_guesses))
                num_of_guesses += 1
        try_again = input("Would you like to try again: [yes/no] ")
else:
        print("Thank you for playing this game!")
