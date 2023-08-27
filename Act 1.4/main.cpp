/**
 * @file mergeSort_main.cpp
 * @author Daniel Hurtado, Gamaliel Marines, Carlos Velasco
 * @brief 
 * @version 0.1
 * @date 2023-08-27
 * 
 * @copyright Copyright (c) 2023
 * 
 */


#include<iostream>
#include<string>
#include <time.h>

using namespace std;

/**
 * @brief Checks if an array is sorted
 * 
 * Complexity: O(n)
 * 
 * @param arr 
 * @param size 
 * @return true 
 * @return false 
 */

bool isSorted(int arr[], int size) {
    // Check if array is sorted
    for (int i = 1; i < size; i++) {
        if (arr[i-1] > arr[i]) {
            return false;
        }
    }
    return true;
}

/**
 * @brief Merges two subarrays of arr[]
 * 
 * Complexity: O(n)
 * 
 * @param arr 
 * @param l 
 * @param m 
 * @param r 
 */

void merge(int arr[], int l, int m, int r) {
    // Merge two subarrays of arr[]
    int n1;
    int n2;
    n1 = m - l + 1;
    n2 = r -m;
    int left[n1];
    int right[n2];

    for(int i = 0; i < n1; i++) left[i] = arr[l + i];

    for(int i = 0; i < n2; i++) right[i] = arr[m + 1 + i];

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
};

/**
 * @brief Sorts an array using merge sort
 * 
 * Complexity: O(nlogn)
 * 
 * @param arr 
 * @param l 
 * @param r 
 */

void mergeSort(int arr[], int l, int r){
    if(l >= r) return;

    int m = l + (r - l) / 2;

    mergeSort(arr, l, m);
    mergeSort(arr, m+1, r);
    merge(arr, l, m, r);
};
/**
 * @brief Main function
 * 
 * @return int 
 */

int main()
{
    // Create array
    int n;
    cout<<"Enter the size of array: ";
    cout << endl;
    cin >> n;
    cout << endl;

    // Check size of array
    if (n <= 0) {
        cout << "Error: The size of the array must be greater than 0" << endl;
        return 0;
    }
    
    int arr[n];   
    srand(time(NULL));   
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 100 + 1;
    }

    cout<<"The original array is: \n";
    // Print array
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    mergeSort(arr, 0, n - 1);
    cout<<endl;
    cout<<"The sorted array is: \n";
    // Print sorted array
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;

    // Test if array is sorted

    if (isSorted(arr, n) == true) {
        cout << "Test Completed: The array is sorted" << endl;
    } else {
        cout << "Test Failed: The array is not sorted" << endl;
    }

    return 0;
};
