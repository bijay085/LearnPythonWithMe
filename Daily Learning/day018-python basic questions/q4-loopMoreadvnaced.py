# Loops advance questions
# 11) strong number
# 12) Tell all the strong number in a range
# 13) tell all the prime numbers in a range
# 14) print the fabionacchi series
# 15)
# Right Triangle - Star
# *
# * *
# * * *
# * * * *
# * * * * *

# 11) strong number
# -> 145 = 1! + 4! + 5! = 145

# factorial code
# -> 2! = 2 , 3! = 3*2*1 , 4!=4*3*1
a = int(input("ENter number :"))
facto = 1
for i in range(a,0,-1):
    facto = facto * i
print(facto)