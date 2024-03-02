# elif condition syntax - this is used there are more number of statements.
"""if CONDITION-1:
        STATEMENT-1 (Will be executed if the condition is true if no jump to next elif line.)
    elif CONDITION-2:
        STATEMENT-2 (It will be executed if CONDITION-2 is true otherwise jump to another elif or else.)
    elif CONDITION-3:
        STATEMENT-3 (It will be executed if CONDITION-3 is true otherwise jump to another elif or else.)
    else
        STATEMENT-4 (It will be executed if all statements are false.)"""

# ********Now time for example******** #
a = int(input("Enter your age i.e value of a :"))
if a >= 20:
    print("You can drive.")
else:
    print("You can't drive.")

# *******Now time for example number 2******* #
b = int(input("Enter your age i.e value of b:"))
if b <= 1:
    print("You are a baby.")
elif b <= 13:
    print("You are more than a teen.")
elif b <= 20:
    print("You are ready to enter in adulthood.")
else:
    print("You are an adult.")
