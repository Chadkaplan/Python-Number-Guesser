import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1, 100)
print(name + ', I am thinking of a number 1-100')

# Ask the player to guess 10 times.
for guessesTaken in range(1, 10):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Too low')
    elif guess > secretNumber:
        print('Too high')
    else:
        break

if guess == secretNumber:
    print('Nice guessing ' + name)
else:
    print('Nope, the answer was ' + str(secretNumber))
