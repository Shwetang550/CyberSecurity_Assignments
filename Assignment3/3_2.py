def func(a,b):
    if(a%2==0 and b%2==0):
        if(a>b):
            return b
        else:
            return a
    else:
        if(a>b):
            return a
        else:
            return b

a=int(input("enter the first number "))
b=int(input("enter the second number "))
print(func(a,b))
