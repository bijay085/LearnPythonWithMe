# *******Example for nested if else statement *******#
# find
word = input("Enter a single alphabet or number of your choice :")
if "z" >= word >= "a" or "Z" >= word >= "A":
    print(word + " letter is an alphabet.")

    if "Z" >= word >= "A":
        print("It is uppercase alphabetic letter.")
    else:
        print("It is lowercase alphabetic letter.")

else:
    print("It is a number.")
