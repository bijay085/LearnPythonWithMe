# for loop work on counter/range Function / number whereas while works on condition

#range function 
# range(s,s,s) : start stop step

#for loop
for i in range(1,20,1):
    print (i)
    
#table of 5 upto 49: 
for i in range(5,50,1): #no need to give 1 , by default it is 1
    result = 5 * i
    print (f"5 x {i} = {result} ")
    
#print odd number from 1 to 100 
for i in range(1,100,2):
    print(i)
    
#print even number from 1 to 100  : use another method
for i in range(1,101):
    if(i % 2 == 0):
        print(i)
        
#reverse for loop
#print from 1000 to 600 (like 1000, 999, 998.....600)
for i in range(1000,599,-1):
    print(i)


