def check(str1):
    u=0
    l=0
    for s in str1:
         if(s.isupper()):
             u=u+1
         elif(s.islower()):
            l=l+1
    return u,l
str1=input("enter the string")
x,y=check(str1)
print("the number of upercase =",x,"number of lowercase = ",y)