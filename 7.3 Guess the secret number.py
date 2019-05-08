# Homework assignment for SmartNinja by Frank Vonk.
secret = 22

guess = int(input("Guess the secret number (between 1 and 30): "))

if guess == secret:
    print("You guessed it - congratulations! :)")
else:
    print("Sorry, your guess is not correct... Secret number is not " + str(guess))
guess = 0
