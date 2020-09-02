def pal(str1):
    if(str1==str1[::-1]):
         return "pallindrome"
    else:
         return "not pallindrome"

str1=input("enter the string ")
print(pal(str1))