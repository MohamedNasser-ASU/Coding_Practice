#include<stdio.h>

double plus(int x, int y);
double mul(int x, int y);
double minus(int x, int y);
double div(int x, int y);


int main(void){

    int x,y , result;
    char c;
    printf("enter first number: ");
    scanf("%d", &x);
    printf("enter second number: ");
    scanf("%d", &y);
    printf("enter Operation, * for multiply , + for add , - for subtract , / for divide: ");
    scanf(" %c", &c);
    switch (c){
        case '+':
            result = plus(x,y);
            break;
        case '-':
            result = minus(x,y);
            break;
        case '*':
            result = mul(x,y);
            break;
        case '/':
            if ( y == 0){
            printf("Can't divide by zero\n");
            return 0;
        } else result = div(x,y);
            break;
        default: 
            printf("Invalid");
    }
    printf("%d", result);



}

double plus(int x, int y){

    return x + y;
}

double mul(int x, int y){

    return x * y;
}

double minus(int x, int y){

    return x - y;
}

double div(int x, int y){

    return x / y;
}
