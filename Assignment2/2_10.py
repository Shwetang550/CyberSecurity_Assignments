x=int(input("enter the number"))
li=[[0 for i in range(x+1)]for j in range(x+1)]
for i in range(1,x+1):
    for j in range(1,i):
        if j==1 or j==i-1:
            li[i][j]=1
        else :
            li[i][j]=li[i-1][j-1]+li[i-1][j]
        print(li[i][j],end=" ")
    print("\n")