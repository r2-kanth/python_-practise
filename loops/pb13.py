'''
*
***
*****

'''





n = int(input("Enter a Number :"))
for i in range(1, n+1):
    print("*"* (2*i - 1) , end ="") # instead of this we can also print("*" * i,end = "")
    print("")
    