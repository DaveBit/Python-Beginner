import random
"""
secret_number = random.randint(0, 10)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
        guess = int(input("Guess: "))
        guess_count +=1
        if guess == secret_number:
            print("You won!")
            break
        else:
            if guess_count < guess_limit:
                print("Try again")
            elif guess_count == guess_limit:
                print("Better luck next time! \nGame ended")
"""

#In Python while loops can also have an else statement. When the while loop completes succesfully with out a break, the else statement takes place.
#Below and alternative way

secret_number = random.randint(0, 10)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
        guess = int(input("Guess: "))
        guess_count +=1
        if guess == secret_number:
            print("You won!")
            break
        elif guess_count < guess_limit:
            print("Try again")
else:
    print("Better luck next time! \nGame ended")
