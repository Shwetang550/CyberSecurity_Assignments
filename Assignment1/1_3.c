//Write a C/C++ program that lists down all the prime numbers in
//a range between a and b, where a and b are two whole numbers.

#include<stdio.h>
int main()
{
    int i,a,b,j,c=0;
    printf("enter a and b");
    scanf("%d %d",&a,&b);
    for(i=a+1;i<b;i++)
    {
      c=0;
      for(j=2;j<=i/2;j++)
      {
          if(i%j==0)
          {
            c++;
          }
      }
      if(c==0)
      {
          printf("%d ",i);
      }

    }
    return 0;
}
