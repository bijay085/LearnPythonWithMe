#---------------------quiz very simple mini project--------------------------#
print("☣️ Welcome to Mini-project -Quiz 🧑‍💻." + " Answer will be yes/no or required output")
score = 0
choice = input("So, ready to play ? y/n : ").lower()

if choice == 'y' or 'yes':
    answer = input(" Q1. Does python have 'do while' loop ?\n").lower()
    if answer== "no":
        print("Corrrect answer")
        score = score+1
    else:
        print("Wrong answer")
        
    answer = input("Q2. Is python case senstive ?\n").lower()
    if answer== "yes":
        print("Corrrect answer")
        score = score+1
    else:
        print("Wrong answer")
        
    answer = input("Q3. How to convert any text to lowercase ?\n").lower()
    if answer== ".lower()":
        print("Corrrect answer")
        score = score+1
    else:
        print("Wrong answer, it is .lower()")

    print(f'Your score is {score}')

else:
    exit()

#we will do this making list so it will increase readability. 