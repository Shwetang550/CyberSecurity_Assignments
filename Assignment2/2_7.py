tup=()
lis=[]

n=int(input("enter the limit"))
for i in range(2,n+1):
    for j in range(2,i):
        if((i%j)==0):
            tup=(i,"not prime")
            break
    else:
        tup=(i,"prime")
    lis.append(tup)
    
print(lis)