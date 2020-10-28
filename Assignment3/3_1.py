def pangram(str):
    s="abcdefghijklmnopqrstuvwxyz"
    for char in s:
        if char not in str.lower():
            print("not pangram")
            return
    else:
        print("pangram")

str=input("enter the string ")
pangram(str)