#include <stdio.h>
#include <stdlib.h>

int ARR_SIZE = 20;


void quicksort(int sort_arr[], int lo, int hi, int size);
int partition(int sort_arr[], int lo, int hi, int size);
void init_arr_from_file(int arr[], char* filepath);

int main(int argc, char** argv) {
    int arr[ARR_SIZE];
    char* filepath;

    filepath = argv[1];

    init_arr_from_file(arr, filepath);
    

    quicksort(arr, 0, ARR_SIZE - 1, ARR_SIZE);

    return 0;
}

void quicksort(int sort_arr[], int lo, int hi, int size) {
    if(lo < hi) {
        int p = partition(sort_arr, lo, hi, size);
        quicksort(sort_arr, lo, p, size);
        quicksort(sort_arr, p+1, hi, size);
    }
    
}

int partition(int sort_arr[], int lo, int hi, int size) {
    for(int i = 0; i < size; i++)
        printf("%d ", sort_arr[i]);    
    printf("\n");
    int pivot = sort_arr[(hi + lo)/2];
    int i = lo - 1;
    int j = hi + 1;
    while(1) {
        do {
            i++;
        } while(sort_arr[i] < pivot);
        do {
            j--;
        } while(sort_arr[j] > pivot);
        if(i >= j)
            return j;
        int temp = sort_arr[i];
        sort_arr[i] = sort_arr[j];
        sort_arr[j] = temp;
    }

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