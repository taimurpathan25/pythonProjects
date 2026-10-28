import random
print("Welcome to the number Guessing Game !")
print("I have a Selected a number between 1 and 100.")

number = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Enter your Guess number : "))
    attempts += 1
    
    if guess < number:
        print("To Low! Try Again")
        
    elif guess > number:
        print("To High! Try Again")
        
    else:
        print(f"Congratulations ! You guessed the number {number}. ")
        print(f"You took {attempts} attempts. ")
        break