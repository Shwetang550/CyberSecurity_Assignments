//Given a string, encrypt this string using # and $ sign, alternatively.

#include<stdio.h>
int main()
{
    int i,j;
    char str[800];
    gets(str);
    for(i=0;str[i]!='\0';i++)
    {
        if(str[i]>=97&&str[i]<=122)
            {
                for(j=0;j<=str[i]-97;j++)
                {
                    if((i+1)%2!=0)
                       printf("#");
                    else
                       printf("$");
                }
            }
        else
            {
                for(j=0;j<=str[i]-65;j++)
                {
                    if((i+1)%2!=0)
                        printf("#");
                    else
                        printf("$");
                }

            }

     }

    return 0;
}
