// practice 1, shopping cart.

#include <stdio.h>
double total( float price, int qty);
int main(void){
    
    char word[128];
    float price;
    int qty;

    printf("What item would you like to buy? ");
    scanf(" %s", word);
    
    printf("What is the price for each? ");
    scanf("%f", &price);      

    printf("How many do you want? ");
    scanf("%d", &qty);

    printf("total = %.2lf ", total(price,qty));

    return 0;
}

double total( float price, int qty){

    return price*qty;
}
