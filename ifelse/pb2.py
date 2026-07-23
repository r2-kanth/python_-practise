s1 =int(input("Enter the first subject marks :"))
s2 =int(input("Enter the Second subject marks :"))
s3 =int(input("Enter the Third subject marks :"))
# Total pecentage formula for the subjects
total_percentage = ((100)*(s1+s2+s3))/300
if(total_percentage > 40 and s1 >= 33 and s2>= 33 and s3 >= 33):
    print("You are passed:", total_percentage)
else:
    print("You are failed:", total_percentage)