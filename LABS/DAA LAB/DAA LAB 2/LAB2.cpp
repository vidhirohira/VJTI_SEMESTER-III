#include <iostream>
#include<algorithm>
using namespace std;

int linearSearch(const int arr[], int size, int target) {
    for (int i = 0; i < size; ++i) {
        if (arr[i] == target) {
            return i; 
        }
    }
    return -1;  
}

int binarySearch(const int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid; 
        }
        else if (arr[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    return -1; 
}

int main() {
    int size;

    cout << "Enter the number of elements in the array: ";
    cin >> size;

    if (size <= 0) {
        cerr << "Array size must be positive." << endl;
        return 1;
    }

    int* arr = new int[size];

    cout << "Enter " << size << " elements:" << endl;
    for (int i = 0; i < size; ++i) {
        cin >> arr[i];
    }

    int target;
    cout << "Enter the number you want to search for: ";
    cin >> target;

    int linearResult = linearSearch(arr, size, target);
    if (linearResult != -1) {
        cout << "Linear Search: Element found at index: " << linearResult << endl;
    } else {
        cout << "Linear Search: Element not found in the array." << endl;
    }
    
    sort (arr, arr + size);

    int binaryResult = binarySearch(arr, size, target);
    if (binaryResult != -1) {
        cout << "Binary Search: Element found at index: " << binaryResult << endl;
    } else {
        cout << "Binary Search: Element not found in the array." << endl;
    }

    delete[] arr;

    return 0;
}