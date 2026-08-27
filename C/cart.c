// practice 1, shopping cart.

#include <stdio.h>

int main(void){
    
    char word[128];
    float price;
    int qty;

    printf("What item would you like to buy? ");
    scanf(" %s", word);
    
    printf("What is the price for each? ");
    scanf("%f", &price);      

    return 0;
}
