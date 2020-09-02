def func(list1):
    list2=[]
    for s in list1:
        if s not in list2:
            list2.append(s)
    return list2
        
n=int(input("enter the no of element in list"))
list1=[]
lis=[]
for i in range(0,n):
    ele=int(input())
    list1.append(ele)

lis=func(list1).copy()
print(lis)