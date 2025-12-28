import random

secret_number = random.randint(1,100)

print("Hey,Welcome to Guess the number!")
print("I am thinking a number between 1 to 100")

attempts = 0

while True:
    guess = int(input("Enter your Guess:"))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    elif guess == secret_number:
        print(f"🎉🥳Congratulations! You guess the correct number in {attempts} attempts. ")
        break
    else:
        print("Guess under the suggested limit")

print("Thank You! Visit again.")
