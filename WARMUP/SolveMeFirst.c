#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int solveMeFirst(int a, int b) {
   int c= a+b;
    return c;
    // Hint: Type return a+b; below
 
}
int main() {
    int num1,num2;
    scanf("%d %d",&num1,&num2);
    int sum; 
    sum = solveMeFirst(num1,num2);
    printf("%d",sum);
    return 0;
}
