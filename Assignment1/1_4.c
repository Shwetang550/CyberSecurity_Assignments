//Write a C/C++ program to encrypt and decrypt the string using
//Caesar Cypher Algorithm.

#include<stdio.h>
int main()
{
    int i,j,choice,k=0;
    char str[500];
    printf("enter the string ");
    gets(str);
    printf("enter the choice\n1-Encrypt\n2-Decrypt");
    scanf("%d",&choice);
    if(choice==1)
    {
        for(i=0;str[i]!='\0';i++)
        {
            if(str[i]>85&&str[i]<=90)
            {
                k=0;
               for(j=90;j>=85;j--)
               {
                   if(str[i]==j)
                   {
                       str[i]=str[i]-25+k+k+4;
                       break;
                   }
                   k++;
               }
            }
            else if(str[i]>=118&&str[i]<=122)
            {

                k=0;
               for(j=122;j>=118;j--)
               {
                   if(str[i]==j)
                   {
                       str[i]=str[i]-25+k+k+4;
                       break;
                   }
                   k++;
               }
            }
           else if((str[i]>=65&&str[i]<=90)||(str[i]>=97&&str[i]<=117))
           {
                 str[i]=str[i]+5;
           }
        }

        printf("the encrypted string is : ");
    }
    else if(choice==2)
    {
       for(i=0;str[i]!='\0';i++)
        {
            if(str[i]>=97&&str[i]<=101)
            {
                k=0;
               for(j=97;j<=101;j++)
               {
                   if(str[i]==j)
                   {
                       str[i]=str[i]+25-4;
                       break;
                   }
                   k++;
               }
            }
            else if(str[i]>=65&&str[i]<=69)
             {
                k=0;
               for(j=65;j<=69;j++)
               {
                   if(str[i]==j)
                   {
                       str[i]=str[i]+25-4;
                       break;
                   }
                   k++;
               }
             }
            else if((str[i]>101&&str[i]<=122)||(str[i]>69&&str[i]<=90))
              {
                 str[i]=str[i]-5;
              }
        }
        printf("the decrypted string is : ");
    }

    puts(str);
    return 0;
}
