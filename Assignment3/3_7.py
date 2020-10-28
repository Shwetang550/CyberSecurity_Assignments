def sum(lis,n):
    s=0
    for i in range(0,n):
        if(lis[i]==6):
            for j in range(i+1,n):
                if(lis[j]==9):
                     i=j+1
                     break
        if(i<n):
            s=s+lis[i]
            if(i==n-1):
                break
        else:
            break

    return s 

lis=[]
n=int(input("enter the limit"))
for i in range(0,n):
    x=int(input())
    lis.append(x)

print(sum(lis,n))