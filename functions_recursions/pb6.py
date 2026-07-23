def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

n = int(input("Enter a number :"))
print(table(n))  #table (5)