import random

top_of_range = input("Type the maximum number: ")

# Check if the input is a valid number
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time!")
        quit()
else:
    print("Only numerical values are allowed!")
    quit()
    
# Generate a random number within the specified range
number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a valid number!")
        continue
    
    if user_guess == number:
        print("Congratulations! You guessed it correctly!")
        break
    
    elif user_guess > number:
        print(f"Your guess {user_guess} is above the number. Try a smaller number.")
    else:
        print(f"Your guess {user_guess} is below the number. Try a larger number.")
        
# Display the number of guesses taken and the correct number
print(f"You guessed the correct number {number} in {guesses} attempts!")
