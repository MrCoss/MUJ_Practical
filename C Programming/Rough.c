#include <stdio.h>

int main(){
  int a, b;
  int *p;
  a=10;
  p = &a;
  b=*p;
  //b = a;
  printf("Value of b is %d", b);
  return 0;
}