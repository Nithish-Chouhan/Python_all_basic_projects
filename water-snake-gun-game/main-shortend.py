import random
'''
1 is snake 
-1 is water 
0 is gun

'''

computer = random.choice([1, -1, 0])
yourchoice = input("enter yuour choice :") 
youdict = {"s":1, "w":-1, "g":0}
reversedict = {1 :"snake", -1:"water", 0:"gun"} 
you = youdict[yourchoice]


print(f"your choice is {reversedict[you]} \n computer choice is {reversedict[computer]}") 


if (computer == you) :
    print("It's a Draw..! try again.") 
else :
    # here in this program  a logic has been implimented and that is between computer choice and you 
    #if the computer chice - you == -1 or 2 then you loose otherwise in all cases you won
    if ((computer-you) == -1 or (computer - you) == 2) :
       print("you lost...")
    else :
       print("you won..")

