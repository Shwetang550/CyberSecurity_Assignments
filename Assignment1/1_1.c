//Write a C/C++ program that takes n numbers from command line
//arguments and finds the least number. In case of invalid entered value
//prompt the user to enter another value.

#include<stdio.h>

int main(int argc, char argv[])
{
    int len=0;

    while(argv[++len] !=NULL);

    int i,arrtemp[len],num=0,alpha=0,special=0;
    char **arr1temp[len];

    for(i=0;i<len-1;i++)
        arr1temp[i]=&argv[i+1];

    for(i=0;i<len-1;i++)
        arrtemp[i]=atoi(argv[i+1]);

    for(i=0;i<len-1;i++)
    {
        if(arr1temp[i]>=48 && **arr1temp[i]<=57)
        num++;

        else if(*arr1temp[i]>=65 && **arr1temp[i]<=90 || **arr1temp[i]>=97 && **arr1temp[i]<=122)
        alpha++;elsespecial++;
    }

    if(alpha>0)
    {
        printf("Please enter number only \n");
        int exit_code;
        exit(exit_code);
    }

    else
    {
        for(i=0;i<len-1;i++)
        {
            int temp=arrtemp[0];
            for(i=0;i<len-1;i++)
            {
                if(temp>arrtemp[i])
                    temp=arrtemp[i];
            }
            printf("Smallest Number is : %d\n",temp);
        }

        printf("\n");
    }

    return 0;
}
