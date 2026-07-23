import random

n = random.choice(range(1, 101))
a = -1 
guesses = 0 
while (a != n ):
    guesses  +=1
    a = int(input("Guess the number : "))
    if (a > n):
        print("Lower number please<-----")
    
    elif (a < n):
        print("Higher number please----->")

print(f"You guessed the correct {n} in the {guesses} guesses")