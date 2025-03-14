// Check whether a given number is prime or not

#include <stdio.h>
// Function to check prime
int isPrime(int num){
  if (num < 2) // Numbers less than 2 are not prime

    return 0;
  for (int i =2; i * i <=num; i++){ // Loop up to sqrt(num)
    if (num % i == 0)
      return 0; // number is divisible hence not a prime
  }
  return 1; // Number is prime  
}

int main(){
  int num;
  // Taking input from the user
  printf("Enter a number:");
  scanf("%d", &num);
  
  //Checking if given number is prime
  if (isPrime(num))
    printf("%d is a prime number\n", num);
  else
    printf("%d is not a prime number\n", num);
  
  return 0;

}