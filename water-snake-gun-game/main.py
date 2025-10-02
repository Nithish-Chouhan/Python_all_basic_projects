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
    if(computer == 1 and yourchoice == -1) :
        print("you lost ...")
    elif(computer == 1 and yourchoice == 0) :
        print("you won ..") 
    elif(computer == -1 and yourchoice == 1) :
        print("you won ..")
    elif (computer == -1 and yourchoice == 0) :
        print("you lost..") 
    elif(computer == 0 and yourchoice == 1) :
        print("you lost ..") 
    elif(computer == 0 and yourchoice == -1) :
        print("you won ..")
    else:
        print("something went wrong..")
