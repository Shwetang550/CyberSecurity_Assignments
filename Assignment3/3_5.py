def func(lis,n):
    for i in range(0,n):
        if(lis[i]==3 and i<n-1):
            if(lis[i+1]==3):
               return "true"
    return "false"

lis=[]
n=int(input("enter the limit"))
for i in range(0,n):
    x=int(input())
    lis.append(x)

print(func(lis,n))