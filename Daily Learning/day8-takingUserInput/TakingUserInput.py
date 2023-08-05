
print("Don't forgot to follow us at insta @Learn.PythonWithMe and join learn python for 100 days.")
print("This the is program where we are going to learn to take user input.")

"""Example number 1 will show how to take input simply."""
print('Example number 1:')
a=input()  #this will take input and store as string.
print("My name is :", a)

"""Example 2nd will show how to prompt message before writing."""
print("Example number 2:")
b=input("Enter your name:") #This will prompt you by saying "Enter your name. This is to clarify."
print("Your name is :", b)

"""Example 3 will show how to take and change input to another data type, by default the taken variable is stored as string."""
print("Enter the 1st input:")
p=input()
print("Enter your 2nd input:")
q=input()
print("The sum is :", p+q)
print("We can see it is concatenating instead of sum.Because it take input as string.So we have to do:")
print("The sum will be :", int(p)+int(q))


