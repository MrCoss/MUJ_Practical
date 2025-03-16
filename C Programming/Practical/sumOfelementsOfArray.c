// C program to find the sum of array elements 

#include <stdio.h>

int main() {
    int n, i, sum = 0;

    // Taking user input for array size
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    int arr[n]; // Declaring the array

    // Taking array elements as input
    printf("Enter %d elements:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);  // Reading elements
        sum += arr[i];         // Adding each element to sum
    }

    // Displaying the sum of array elements
    printf("Sum of array elements: %d\n", sum);

    return 0;
}

