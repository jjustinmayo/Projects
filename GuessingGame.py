#try:
    #import random
    #print("success")
    
#except:
    #print("fail")

    
import random

number = random.randint(0,10)

lives = 3

while lives > 0:
    answer = input("enter number: ")
    if(answer == number):
        print("correct")
    else: 
        lives -= 1
        print("wrong... you have", lives," more lives")

else: 
    print ("fuck off")
    

#ctrl-/ => comment everything
