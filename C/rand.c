// practice 4, random number guesser.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void){
    srand(time(NULL));

    int guess = 0;
    int tries = 0;
    int min   = 1;
    int max   = 100;
    
    int random = (rand() % (max - min +1)) + min;
    do {
        
        printf("Guess the number: ");
        scanf(" %d", &guess);
        tries++;
        if ( guess > random)
            printf("Too high\n");
        else 
            printf("Too low\n");

    } while (guess != random);

    printf("Correct! %d was the number.\n tries = %d", guess, tries);

    return 0;
}
