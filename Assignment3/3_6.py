def func(a,b,c):
    if((a+b+c)<=21):
        return a+b+c
    elif((a+b+c)>21 and (a==11 or b==11 or c==11)):
        return a+b+c-10
    elif((a+b+c)>21):
        return "BUST"

a=int(input("first number"))
b=int(input("second number "))
c=int(input("third number "))
print(func(a,b,c))