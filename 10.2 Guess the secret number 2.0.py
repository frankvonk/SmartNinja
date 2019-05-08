# Homework assignment for SmartNinja by Frank Vonk.
import random


def main():
    while True:
        secret = random.randint(0, 22)

        guess = int(input("Guess the secret number (between 1 and 22): "))

        if guess == secret:
            print("You guessed it - congratulations! :)")
            break
        else:
            print("Sorry, your guess is not correct... Secret number is not " + str(guess))


if __name__ == '__main__':
    main()
