def func(n):
    c=0
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if(i%j==0):
                break
        else:
            c=c+1
    return c

n=int(input("enter the number "))
print("the no. of prime numbers are : ",func(n))