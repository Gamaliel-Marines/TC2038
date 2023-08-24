#include<iostream>
#include<string>

using namespace std;


void printArray(int arr[], int size){
    for(int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";

    }
    cout << endl;
}

void mergeSort(int arr[], int l, int r);

void merge(int arr[], int l, int m, int r);

int main()
{
    int n;
    
    std::cout << endl;
    std::cout<<"Enter the size of array: ";
    std::cin >> n;
    std::cout << endl;
    
    int arr[n];      
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 100 + 1;
    }

    cout<<"The original array is: \n";
    printArray(arr, n);
    mergeSort(arr, 0, n - 1);
    cout<<endl;
    cout<<"The sorted array is: \n";
    printArray(arr, n);
    cout << endl;

    return 0;
}

void mergeSort(int arr[], int l, int r){
    if(l >= r)
    {
        return;
    }
    int m = l + (r - l) / 2;
    mergeSort(arr, l, m);
    mergeSort(arr, m+1, r);

    merge(arr, l, m, r);
}

void merge(int arr[], int l, int m, int r) {
    int n1;
    int n2;

    n1 = m - l + 1;
    n2 = r -m;

    int left[n1];
    int right[n2];

    for(int i = 0; i < n1; i++)
    {
        left[i] = arr[l + i];
    }

    for(int i = 0; i < n2; i++)
    {
        right[i] = arr[m + 1 + i];
    }

    int i = 0;
    int j = 0;
    int k = l;

    while(i < n1 && j < n2)
    {
        if( left[i] <= right[j])
        {
            arr[k] = left[i];
            i++;
        }

        else
        {
            arr[k] = right[j];
            j++;
        }
        
        k++;

    }
    
    while (i < n1) {
        arr[k] = left[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = right[j];
        j++;
        k++;
    }

}
