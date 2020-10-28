def func(n):
    if(n>=90 and n<=110):
        return "true"
    elif(n>=190 and n<=210):
         return "true"
    
    return "false"

n=int(input("enter the number "))
print(func(n))