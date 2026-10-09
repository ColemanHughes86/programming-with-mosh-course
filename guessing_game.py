import random

secret_number = random.randint(1,100)
guess_count = 0
guess_limit = 10

while guess_count < guess_limit:
    guess = int(input('Enter your guess from 1 - 100: '))
    guess_count += 1
    if guess == secret_number:
        print('You win')
        break
    elif guess > secret_number:
        print('Your guess is too high')
    elif guess < secret_number:
        print('Your guess is too low')
    elif guess_count == guess_limit and guess != secret_number:
        print('Out of guesses')
