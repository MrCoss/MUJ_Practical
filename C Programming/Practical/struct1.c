// Write a C program using structure to store details about a book (Title, Author, yearPublished, price)

#include <stdio.h>

// Define a structure for a book
struct Book {
    char title[100];
    char author[100];
    int yearPublished;
    float price;
};

int main() {
    struct Book book1;

    // Taking user input for book details
    printf("Enter Book Title: ");
    fgets(book1.title, sizeof(book1.title), stdin);

    printf("Enter Author Name: ");
    fgets(book1.author, sizeof(book1.author), stdin);

    printf("Enter Year Published: ");
    scanf("%d", &book1.yearPublished);

    printf("Enter Price: ");
    scanf("%f", &book1.price);

    // Displaying book details
    printf("\nBook Details:\n");
    printf("Title: %s", book1.title);
    printf("Author: %s", book1.author);
    printf("Year Published: %d\n", book1.yearPublished);
    printf("Price: %.2f\n", book1.price);

    return 0;
}
