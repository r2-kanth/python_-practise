with open("log.txt" ,) as f:
    lines = f.readlines()
    lineno = 1
for line in lines:

    if("python" in line ):
        print(f"Python word was present in the content . Line no : {lineno}")
    lineno +=1

else:
    print("Python word was not present in the content ")
