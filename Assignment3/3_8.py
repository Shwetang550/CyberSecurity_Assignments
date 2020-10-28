def func(lis,n):
    list=[0,0,7]
    k=0
    for i in list:
        for j in range(0+k,n):
            if(i==lis[j]):
                k=j+1
                break
        else:
            return "false"
    return "true"
    

lis=[]
n=int(input("enter the limit"))
for i in range(0,n):
    x=int(input())
    lis.append(x)

print(func(lis,n)) 