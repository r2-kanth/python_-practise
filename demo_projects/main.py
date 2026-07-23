''''
1 = snake
0 = gun
-1 = water

'''
import random
computer = random.choice([1, 0 , -1])
n=int(input("Enter the number of rounds you want to play : "))
won = 0
loose = 0

for i in range(n):
    youstr = input("Enter your choice : ")
    youdict = {"s" : 1 , "g" : 0 , "w" : -1 }
    reversedict = {1 : "Sanke " , 0 : "Gun" , -1 : " Water"} 
    you = youdict[youstr]
    print(f"You choose {reversedict [you]} \n Computer choose {reversedict [computer]}")

    if(computer == you):
        print("Its a Draw")

    else:
        if(computer == 1 and you == 0 ):
            print("You won !")
            won += 1
        elif(computer == 1 and you == -1):
            print("You loose")
            loose += 1
        elif(computer == 0 and you == -1):
            print("You won!")
            won += 1
        elif(computer == 0 and you == 1):
            print("You loose")
            loose += 1
        elif(computer == -1 and you == 1):
            print("You win!")
            won += 1
        elif(computer == -1 and you == 0):
            print("You loose")
            loose += 1
        else:
            print("Something went wrong")

print(f"You won {won} times and loose {loose} times")