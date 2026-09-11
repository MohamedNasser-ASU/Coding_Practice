#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <wait.h>

int handle_redirect(char *args[]);

int main(int argc, char *argv[])
{
    int script = 0;
    if (argc >1){
    
        if (freopen(argv[1], "r", stdin) == NULL){
            fprintf(stderr, "Can't read from script file %s\nExiting..", argv[1]);
            exit(1);
        }
        script = 1;
    }


    while(1){

        // string to hold command
        char buffer[1024];

        // prompt
        if (!script)
            printf("$ ");

        //take command from user
        if ( fgets(buffer, 1024, stdin) == NULL ) break;

        //trim newline
        char *nl = strchr(buffer, '\n'); // search for newline in the buffer
        if (nl) *nl = '\0';
        
        // if in script mode
        // remove comments from script file
        char *hash = strchr(buffer, '#');
        if (hash) *hash = '\0';


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
            // see if user wants redirection
            if ( handle_redirect(args) == -1 ) {
                fprintf(stderr, "redirection failed");
            }
            // execute args from buffer
            execvp(args[0], args);
        }

    }

}
// 1 if success
// 0 if no redirect
// -1 if failed
int handle_redirect(char *args[]){
    for(int i = 0; args[i] != NULL; i++){
        if ( strcmp(args[i], ">") == 0 ) { // '>' found in user's prompt
            // assume next arg is the file to write to
            if (freopen(args[i+1], "w", stdout) == NULL ) return -1;
            // terminate the rest of the command after ">"
            args[i] = NULL;
            return 1;
        }
    }
    return 0;
}
