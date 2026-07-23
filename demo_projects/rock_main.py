''''
1 = rock
0 = paper
-1 = scissors


'''
import random
computer = random.choice([1, 0 , -1])
youstr = input("Enter your choice : ")
youdict = {"r" : 1 , "p" : 0 , "s" : -1 }
reversedict = {1 : "Rock " , 0 : "Paper" , -1 : "Scissors"} 
you = youdict[youstr]

print(f"You choose {reversedict [you]}\n Computer choose {reversedict [computer]}")

if(computer == you):
    print("Its a Draw")

else:
    if(computer == 1 and you == 0 ):
        print("You won !")
    elif(computer == 1 and you == -1):
        print("You loose")
    elif(computer == 0 and you == -1):
        print("You won!")
    elif(computer == 0 and you == 1):
        print("You loose")
    elif(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You loose")
    else:
        print("Something went wrong")