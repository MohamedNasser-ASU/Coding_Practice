#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <wait.h>

int main(int argc, char *argv[])
{
    while(1){

        // string to hold command
        char buffer[1024];

        // prompt
        printf("$ ");

        //take command from user
        fgets(buffer, 1024, stdin);

        //trim newline
        char *nl = strchr(buffer, '\n'); // search for newline in the buffer
        if (nl) *nl = '\0';

        // split buffer into args
        char *args[20];
        int nargs = 0;
        args[nargs]= strtok( buffer, " ");
        while ( args[nargs] != NULL ){
            args[++nargs]= strtok(NULL, " ");
        }
    
        // if the user clicked enter with no commands
        if (args[0] == NULL) continue;

        // if user typed exit, exit
        if (strcmp(args[0], "exit") == 0) exit(0);

        // fork and exec
        pid_t pid = fork();

        if (pid > 0){
            // we are in parent
            wait(NULL);
        }
        else if (pid == 0){
            // we are in child
            // execute args from buffer
            execvp(args[0], args);
        }

    }

}
