print("")
"""string are immutable in python."""
a = "$$PythoN!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.rstrip("$"))
"It doesn't remove the starting sign that is $."
"""If we want to replace the string."""
print(a.replace("$$PythoN!!", "Patrick"))
print(a.split(" "))
