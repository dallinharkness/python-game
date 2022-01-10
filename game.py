"""A number-guessing game."""
import random
attempts = 0
randonumbo = random.randint(1,100)
# Put your code here
print("Hello there! What is your name?")

name = input('Insert name...')

print(name + ', guess a number between 1-100')

while True:#a while statement to continuing loop the numbers
    guess = int(input('Insert number...'))

    if guess < 1 and guess > 100:
        print('Please guess a number between 1 and 100...')

    attempts += 1#counting each time you guess

    if guess < randonumbo:
        print('The number is higher keep trying!')
    elif guess > randonumbo:
        print('The number is lower, keep trying!!')

    else:
        print('Congrats! You go it!')
        print(f'It took you {attempts} wow!')
        break



