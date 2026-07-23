f = open("poem.txt")
data = f.read()
print(data)
if("Twinkle" in data ):
    print("Twinkle is present in this contant")
else:
    print("Twinkle is not present in this content ")
f.close()