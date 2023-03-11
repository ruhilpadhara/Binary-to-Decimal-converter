from os import system, name
import time
def clear(): 
  
    
    if name == 'nt': 
        _ = system('cls') 
  
    
    else: 
        _ = system('clear')
clear()
num=input("Please enter your decimal here:")
bin=0
divisionControl=int(num)

total= []

if(int(num)<0):
    print("This is not a positive number.\n") 

#Calculate
for i in range(1,99):
    bin = int(divisionControl)%2
    divisionControl = int(divisionControl)//2
    if(int(divisionControl)==0):
        break
    total.append(str(bin))
#Reverse's numbers
total.reverse()
#Output
clear()
print("Your input decimal is ", num)
print("Your binary is")
print("1",end="",sep="")
for i in total:
    print(str(i),sep="",end="")
print()
time.sleep(6)
exec(open('BinCalculator.py').read())
