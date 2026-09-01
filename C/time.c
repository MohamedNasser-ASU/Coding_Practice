#include <stdio.h>
#include <time.h>
#include <unistd.h>

int main(void){
    while(1){
        // retuns cursor back to the prev. line
        printf("\x1b[1F");    
        // clears the line
        printf("\x1b[2K");
        // gets current time in seconds from EPOC
        time_t timeNow_s = time(NULL);
        //calculate time and return it in a timestring
        char *timestring = ctime(&timeNow_s);
        printf("%s", timestring);
        usleep(100000);
    }
}
