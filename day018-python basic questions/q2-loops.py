# # Loops question
# # 1) Print natural number up to n.
# # 2) Reverse for loop. Print n to 1.
# # 3) Take a number as input and print its table
# # 5*1 = 5
# # 5*2= 10... up to 10 terms.
# # 4) Sum up to n terms.
# # 5) Factorial of a number.

# # # 1) Print natural number up to n.
# n = int(input("ENter n : "))
# for i in range(1,n+1,1):
#     print (i)
# print ("\n")

# # # 2) Reverse for loop. Print n to 1.
# for i in range(n,0,-1):
#     print(i)
    
# # 3) Take a number as input and print its table
# # 5*1 = 5
# # 5*2= 10... up to 10 terms.
# mul = int(input("Enter multipler :\n"))
# num = int(input("Till which number : \n"))
# for i in range(1,num+1,1):
#     result = mul * i
#     print(f"{mul} x {i} = {result}")

# 4) Sum up to n terms.
# num2 = int(input("ENter the nth term :"))
# sum = 0
# for i in range(1,num2+1,1):
#     sum = sum + i
#     print(sum)

# 5) Factorial of a number.
num3 = int(input("ENter the number of which u want factorial :"))
factorial = 1
for i in range(num3,1,-1):
    factorial = factorial * i
print(factorial)
    