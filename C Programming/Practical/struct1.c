// Write a C program using structure to store details about a book (Title, Author, yearPublished, price)

#include <stdio.h>

struct Book {
  char name[50];
  char author[50];
  int yearPublished;
  int price;
};

int main(){
 struct Book bk;
 printf("Enter Book name, author, yearPublished, price\n");
 scanf("%s\n", bk.name);
 scanf("%s\n", &bk.author);
 scanf("%d\n", &bk.yearPublished);
 scanf(" %d\n", &bk.price);

 printf("Book Name: %s\n",bk.name);
 printf("Author: %s\n",bk.author); 
 printf("Year of Published: %d\n",bk.yearPublished);
 printf("Price: %d\n",bk.price);

}
