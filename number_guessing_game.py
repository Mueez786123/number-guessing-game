import random

number = random.randint(1,10)

attempts = 0
guess = None

print("🎮 Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print("You Have only 3 attempts")
while guess != number:
    guess = int(input("Enter your Number: "))
    attempts += 1
    if attempts == 3:
        print("You lost")
        print("the number was :", number)
        break
        
    if guess > number:
        print('Too High')
    elif guess < number:
        print("too low")     
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        