import random
x = random.randint(1,10)


print("**********Welcome To The Number Guessing Game**********")

def get_valid_guess():
    while True:
        try:
            guess = int(input("Enter any number from 1 to 10: "))
            return guess
        except ValueError:
                print("Not an integer, try again!")
                continue
        else:
            break

wrong_guess = get_valid_guess()            
num_of_guesses = 1


while wrong_guess != x:
    try:
        if wrong_guess <= 0 or wrong_guess > 10:
            print("Guess a number from 1 to 10")
            guess = int(input("Enter any number from 1 to 10: "))
            num_of_guesses += 1
        elif wrong_guess < x:
            print("You should guess higher")
            guess = int(input("Enter any number from 1 to 10: "))
            num_of_guesses += 1
        elif wrong_guess > x:
            print("You should guess lower")
            guess = int(input("Enter any number from 1 to 10: "))
            num_of_guesses += 1
    except ValueError:
        wrong_guess
            
            
if wrong_guess == x:
    print("You guessed it correctly, congratulations!!!")
    print("It took you {} tries to guess the correct number.".format(num_of_guesses))
    num_of_guesses += 1


try_again = "yes"
try_again = input("Would you like to try again: [yes/no] ")

while try_again == 'yes':
        x = random.randint(1,10)
        guess = int(input("Please pick any number from 1 to 10: "))
        num_of_guesses = 1
        while wrong_guess != x:
            try:
                if wrong_guess <= 0 or wrong_guess > 10:
                    print("Please only guess a number from 1 to 10")
                    guess = int(input("Please pick any number from 1 to 10: "))
                    num_of_guesses += 1
                elif wrong_guess < x:
                    print("You should guess higher")
                    guess = int(input("Please pick any number from 1 to 10: "))
                    num_of_guesses += 1
                elif wrong_guess > x:
                    print("You should guess lower")
                    guess = int(input("Please pick any number from 1 to 10: "))
                    num_of_guesses += 1
            except:
                wrong_guess

        if wrong_guess == x:
                print("You guessed it correctly, congratulations!!!")
                print("It took you {} tries to guess the correct number.".format(num_of_guesses))
                num_of_guesses += 1
        try_again = input("Would you like to try again: [yes/no] ")
else:
        print("Thank you for playing this game!")
