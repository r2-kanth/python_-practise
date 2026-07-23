n=int(input("Enter the numebr :"))
if( n >0):
    a =1
    for i in range(1, n+1):
        a= a*i
    print(f"Factorial of a given number is {a}")
else:
    print("Enter the positive number may be your entered the invalid number")