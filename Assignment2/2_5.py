def mul(list):
    s=1
    for i in list1:
        s=s*i
    return s

n=int(input("enter the number of element in list"))
list1=[]
for i in range(0,n):
    ele=int(input())
    list1.append(ele)

print("result : ",mul(list1))