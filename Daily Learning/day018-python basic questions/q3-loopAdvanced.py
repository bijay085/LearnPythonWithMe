# Loops advance questions
# 6) Print all the factors of a number.
# 7) Accept a number and check if it a perfect number or not.
# A number whose sum of factors(excluding number itself)
# = Number
# Ex - 6 = 1, 2, 3 = 6
# 8) Check if the number is Prime or not.
# 9) Seprate each digit of a number and print it on the new line
# 10) Accept a number and check if it is a pallindromic number
# (If number and its reverse are equal)
# Ex - 12321 - Rerverse - 12321

# 6) Print all the factors of a number.
num1 = int(input("Enter the number of you u want the factor :"))
factor = 0

for i in range(1,num1+1,1):
    if(num1%i==0):
        print(i)
        
# 7) Accept a number and check if it a perfect number or not.
num2 = int(input("Enter any number :"))
factors = 0

for i in range(1,num2,1):
    temp = num2
    if(num2%i==0):
        factors = factors+i
        
if(temp == factors):
    print(f"It, {num2} is perfect number.\n")
else:
    print(f"It, {num2} is not a perfect number.\n")
    
# 8) Check if the number is Prime or not.
# -> A trick : if the factorails are more than 2 than it is not prime number.
num3 = int(input("Enter the number to check it is prime or not : "))
count = 0
for i in range(1,num3+1,1):
    if(num3 % i == 0):
        # print(i)
        count = count +1
print(count)
if(count <= 2):
    print(f"{num3} is a prime number.\n")
else:
    print(f"{num3} is not a prime number.")
    
# 9) Seprate each digit of a number and print it on the new line
num4 = int(input("Enter the number : "))
while(num4):
    mod = num4 % 10
    print(mod)
    num4 = num4 // 10  
    
# 10) Accept a number and check if it is a pallindromic number
# (If number and its reverse are equal)
# Ex - 12321 - Rerverse - 12321
num5 = int(input("Enter number to check palindrome :"))
temp = num5
res = 0
while(num5>0):
    mod = num5 % 10
    res = res* 10 + mod
    num5 = num5 // 10
# print(res)
    
if(temp == res):
    print(f"{temp} is palindrome. \n")
else:
    print(f"{temp} is not palindrome. \n")