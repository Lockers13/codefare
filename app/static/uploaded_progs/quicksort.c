#include <stdio.h>

void quicksort(int sort_arr[], int lo, int hi, int size);
int partition(int sort_arr[], int lo, int hi, int size);

int main(int argc, char** argv) {
    int sort_arr[] = {1,4,5,3,7,6,19,2,9,16,11};
    int arr_size = sizeof(sort_arr)/sizeof(sort_arr[0]);

    quicksort(sort_arr, 0, arr_size - 1, arr_size);
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
    
