def func(n1,n2,num):
       if(num not in range(n1,n2+1)):
           return "not in range"
       else:
           return "number is in given range"

num=int(input("enter the number"))
print("enter the range")
n1=int(input())
n2=int(input())
print(func(n1,n2,num))
