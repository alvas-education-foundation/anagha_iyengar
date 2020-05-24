PROGRAM 1
/* WriteaCProgram toDisplayfirstNTriangularNumbers(WhereNisreadfrom the
Keyboard)*

#include<stdio.h>
voidtriangular_series(intn)
{
for(inti=1;i<=n;i++)
printf("%d",i*(i+1)/2);
}
intmain()
{
intn;
printf("Entervalueforn");
scanf("%d",&n);
triangular_series(n);
return0;
} 