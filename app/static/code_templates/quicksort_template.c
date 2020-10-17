#include <stdio.h>
#include <stdlib.h>

/* The below code template initializes an array read from the .txt 
file you have just downloaded. Now it is up to you to quicksort it
and produce the specified output. Do not change any of the template
code provided or else your code will not run in our testing environment */


int ARR_SIZE = 20;

void init_arr_from_file(int[], char*);

int main(int argc, char** argv) {
    int arr[ARR_SIZE];
    char* filepath;
    
    filepath = argv[1];
    init_arr_from_file(arr, filepath);

    // the variable arr can now be used freely...


    return 0;
}

void init_arr_from_file(int arr[], char* filepath) {
    FILE *fp;
    int i;

    fp = fopen(filepath, "r");

    if (fp == NULL){
        printf("Error Reading File\n");
        exit(0);
    }

    for (i = 0; i < ARR_SIZE; i++){
        fscanf(fp, "%d\n", &arr[i] );
    }

    fclose(fp);
}