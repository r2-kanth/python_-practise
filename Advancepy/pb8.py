def Div(num):
    if(num % 5 ==0):
        return True
    return False

a = [44, 555, 666, 766,57  , 87 , 555, 45 , 85]

f= list(filter(Div, a))
print(f)