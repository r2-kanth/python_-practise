def inch(n):
    return n/2.54

n = float(input("Enter the inches : "))
c = inch(n)
print(f"{round (c,2)} in centtimeters")