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
        print('Too low, ' + str(10-guessesTaken) + ' guesses remaining')
    elif guess > secretNumber:
        print('Too high, ' + str(10-guessesTaken) + ' guesses remaining')
    else:
        break

if guess == secretNumber:
    print('Nice guessing ' + name +', you guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope, the answer was ' + str(secretNumber))