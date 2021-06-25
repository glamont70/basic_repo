 #Print all integers from 0 - 150
for num in range(0,150,1):
    print(num)
    
 #Print all the multiples of 5 from 5 to 1,000
for num in range(5,1000,5):    
    print(num)
    
 #Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".  
for num in range(1,100,1):
    if num % 10 == 0:
        print("Coding Dojo")  
    elif num % 5 == 0:
        print("Coding")   
    else:
        print(num)
        
 #Add odd integers from 0 to 500,000, and print the final sum.
sum = 0 
for num in range(0,500000,1): 
   if(num % 2 !=0): 
      sum=sum + num 
print(num) 

 #Print positive numbers starting at 2018, counting down by fours.
for num in range(2018,0,-4):
    print(num)
    
 #Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum,highNum+1,1):
    if(num % mult == 0):
        print(num)