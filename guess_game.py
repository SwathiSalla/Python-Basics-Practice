import random
number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
while guess != number:
    if guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 100: "))
print("Congratulations! You guessed the number.")