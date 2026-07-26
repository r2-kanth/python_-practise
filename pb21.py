def prime(num):
    if (num <= 1):
        return False

    for i in range(2, num+1):
        if(num % i == 0 ):
            return False
        return True

num = int(input("enter a number : "))

if prime(num):
    print("prime number")

else:
    print("Not a prime Number")