def func(t):
    for i in t:
         for j in i:
            print(j,end=" ")
         print()
    for s in range(0,5):
        print("player 1(X) : enter the row and column :")
        a=int(input())
        b=int(input())
        if(a==1):
            a=a-1
        elif(a>2):
            a=a+1
        if(b==1):
            b=b-1
        elif(b>2):
            b=b+1
        t[a][b]="X"
        
        for i in t:
            for j in i:
                print(j,end=" ")
            print()
        for i in t:
            c=0
            for j in i:
              if(j!="|"):
                if(j=="X"):
                    c=c+1
                    if(c==3):
                      print("player 1 wins")
                      return
        for i in range(0,5):
            c=0
            for j in range(0,5):
                if(t[j][i]=="X"):
                    j=j+1
                    c=c+1
                    if(c==3):
                        print("player 1 wins")
                        return
        if(t[0][0]==t[2][2]==t[4][4]=="X"):
                print("player 1 wins")
                return
        if(t[0][4]==t[2][2]==t[4][0]=="X"):
                print("player 1 wins")
                return
        if(s<4):
            print("player 2 (0): enter the row and column :")
            a=int(input())
            b=int(input())
            if(a==1):
               a=a-1
            elif(a>2):
               a=a+1
            if(b==1):
               b=b-1
            
            elif(b>2):
                b=b+1
            t[a][b]=0
            
        
            for i in t:
               for j in i:
                  print(j,end=" ")
               print()
            for i in t:
               c=0
               for j in i:
                 if(j!="|"): 
                   if(j==0):
                     c=c+1
                     if(c==3):
                       print("player 2 wins")
                       return
            for i in range(0,5):
               c=0
               for j in range(0,5):
                   if(t[j][i]==0):
                     c=c+1
                     if(c==3):
                        print("player 1 wins")
                        return  
            if(t[0][0]==t[2][2]==t[4][4]==0):
                print("player2 wins")
                return
            if(t[0][4]==t[4][0]==0):
                print("player 2 wins")
                return
    else:
        print("draw")
        return
        
t=[[" ","|"," ","|"," "],["_","_","_","_","_"],[" ","|"," ","|"," "],["_","_","_","_","_"],[" ","|"," ","|"," "]]
func(t)