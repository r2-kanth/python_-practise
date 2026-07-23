n = int(input("Enter a Number : "))
for i in range(2,n):
    if(n%i == 0):
        print("The number is not prime number")
        break

else:
    print("The number is prime number")