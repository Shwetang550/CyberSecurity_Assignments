d=dict()
lis=[]
c=0
n=int(input("enter the limit"))
for i in range(2,n+1):
    for j in range(2,i):
        if((i%j)==0):
            d[i]=("not prime")
            break
    else:
        d[i]=("prime")
print(d)
    
for i in range(2,n+1):
    if(d[i]=="not prime"):
        del d[i]
        c=c+1;
print(d)
print("count of non prime is : ",c)