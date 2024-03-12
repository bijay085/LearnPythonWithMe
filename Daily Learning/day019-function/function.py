#Function is a block of code used to execute any task. It will run when it is called. 
#A function can be defined using the 'def' keyword followed by the name of the function and parentheses containing the (maybe) parameters.

"""
Syntax of the function

def functionName(parameter):
    //code to be excuted
    
functionName(Argument) 
"""

#A function can be of 4 types : The very basic example are :

#1st type : Normal parameter function
def greet(a,b,c): 
    print(a+b+c)
    
greet(1,2,4) #7


#2nd type: default parameter
def greet(a,b,c,d=5):
    print(a+b+c+d)

greet(1,2,3) #11


#3rd type : Deafult agrument : same as normal parameter

#4th type : keyword argument
def greet(a,b,c,d=10):
    print(a+b+c+d)

greet(b=1, c=3, a=1)  #15 -> it will assign the values as mentioned in arguemnt section


# print vs return 
#print
def MyName(name):
    print(name) #prints whatever you pass into the function
    
MyName("Python")
#=> It will simply print name but not return anything.

# return 
def MyName(name):
    return name #returns what ever you pass into the function where we had called this function
    
MyName("Python") # return name : return the value here but didnt get print cuz we hadnt call print yet

print(MyName("Python")) # it will get the value after return statment the print function print here.


#example of function
#find the number is even or odd , the number can be many 
def oddEven(num):
    if(num % 2 == 0):
        return (f"{num} is even. \n")
    else:
        return (f"{num} is odd.\n")
    #we can also store the value :be careful for indent
    
result = oddEven(12)
print(result)
    
#or we can directly print
print(oddEven(6))
print(oddEven(1))
print(oddEven(79))