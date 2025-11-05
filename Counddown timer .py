# Countdown Timer 
# import time 
import time   

# step 1 get user input for countdown start 
start = int(input("Enter the countdown number to start:")) 

# step 2 countdown using a while loop 
print ("\n---Countdown begins---")
while start >0 :
   print (start)
   start -=1
   time.sleep (1)
# step 4 print final message 
print ("\n---countdown complete---")

 