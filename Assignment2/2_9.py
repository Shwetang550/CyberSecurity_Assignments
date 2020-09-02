import sys
n=int(sys.argv[1])
a,b=0,1
print(a)
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c