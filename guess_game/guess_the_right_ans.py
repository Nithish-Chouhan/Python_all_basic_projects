#this is the game of guessing right ans
import random

n = random.randint(1, 100)
a = -1
guess = 0
while(a != n):
    guess += 1
    a = int(input("guess the number...: "))
    
    if(a >= n):
        print("guess lower number...")
    else:
        print("higher number please..")

print(f"correct. you got the right number : {n} in {guess} attempts")