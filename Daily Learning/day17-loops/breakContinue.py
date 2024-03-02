# #break is used to break the loop even if the conditon == true 
# #continue is used to continue the loop even if the condition == false

# #without break : 1,2,3...199
# a = 18
# for i in range(1,200,1):
#     # i = i+2
#     print(i)
#     # break
   
# #with break : 1
# # a = 18
# for i in range(1,200,1):
#     # i = i+2
#     print(i)
#     break

# # question :upto 100 even numbers if u found "50" break, counting goes on until 100 even numbers
# count = 0
# even = 0
# while (count<=100):
#     even = even + 1
#     if(even % 2==0):
#         print(even)
#         count = count + 1
#         if(even == 50):
#             break   # it will break the statement process if 50 is found
        
#continue

for i in range(1,11):
    print(i)        #output 1 2 3 4 5 6 7 8 9 10 


for i in range(1,11):
    if(i==5):
        break
    print(i)       #output 1 2 3 4 
 
   
for i in range(1,11):
    if(i==5):
        continue
    print(i)        #output 1 2 3 4  6 7 8 9 10 
    
    