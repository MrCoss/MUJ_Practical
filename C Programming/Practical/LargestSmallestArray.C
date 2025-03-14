// find largest & smallest from array.

#include <stdio.h>

int main() {
  int n, i, largest, smallest;

  //Taking input for array size
  printf("Enter the number of elements in the array: ");
  scanf("%d", &n);
  int arr[n];

  // Taking array elements input and storing it
  printf("Enter %d elements for array: \n", n);
  for (i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
  }

  //Initialize largest and smallest with the first element
  largest = smallest = arr[0];

  //Finding largest and smmallest element
  for (i = 1; i < n; i++){
    if (arr[i]>largest){
      largest = arr[i]; // Update largest if current element is greater than initialized element 
    }
    if (arr[i] < smallest){
      smallest = arr[i]; //Update smallest if current elemet is smaller than initialized element
    }
  }
  // Displaying results
  printf("largest element: %d\n", largest);
  printf("Smallest element is %d\n", smallest);

}
