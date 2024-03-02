# Raw string and formatted string

# 1st : Raw string
print("If we want to print escape sequnce \n , \t \b etc etc, we can't.")
#if we put r we can print same to same inside written inside "".
print(r"If we want to print escape sequnce \n , \t \b etc etc, we can't.")

#formatted string
name = "John The Don"
age = 20
# method 1 
print("His name is ", name, "and age is ", age ,".")

# method 2
print(f"His name is {name} and age is {age}")