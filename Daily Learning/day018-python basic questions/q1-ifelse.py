# If Else questions
# 1)Accept two numbers and print the greatest between them
# 2)Accept the gender from the user as char and print the
# respective greeting message
# Ex - Good Morning Sir (on the basis of gender)
# 3)Accept an integer and check whether it is an even number
# or odd.
# 4)Accept name and age from the user. Check if the user is a
# valid voter or not.
# 5)Accept a year and check if it a leap year or not
# 6)Accept an English alphabet from user and check if it is a
# consonant or a vowel

# 1)Accept two numbers and print the greatest between them
a = int(input("Enter 1st number : \n"))
b = int(input("Enter 2nd number : \n"))

if(a>b):
    print(f"a. {a} is greater")
else:
    print(f"b. {b} is greater")
    
# 2)Accept the gender from the user as char and print the respective greeting message
gender = input("What is your gender ? f/m \n")
if(gender == "f"):
    print("Good morning miss")
elif (gender == "m"):
    print("Good morning sir.")
else:
    print("Please enter m or f otherwise invalid")
    
# 3)Accept an integer and check whether it is an even number or odd.
num = int(input("Enter a number :"))
if(num%2==0):
    print(f"{num} is even.\n")
else:
    print(f"{num} is odd.")
    
# 4)Accept name and age from the user. Check if the user is a valid voter or not.
name = input('Enter your name : \n')
age = int(input('ENter your age :\n'))

if(age>=18):
    print(f"{name} can vote.\n")
else:
    print(f"{name} can't vote.\n")
    
#  5)Accept a year and check if it a leap year or not
# any year which is divisble by 4 is a leap year 
year = int(input("Input the year :\n"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print('It is leap year.')
else:
    print("It is not a leap year.\n")
    
# 6)Accept an English alphabet from user and check if it is a consonant or a vowel
alph = input("Enter any single letter :\n")
if(alph in "aeiouAEIOU"):
    print("It is vowel.")
else:
    print("It is consonent.\n")