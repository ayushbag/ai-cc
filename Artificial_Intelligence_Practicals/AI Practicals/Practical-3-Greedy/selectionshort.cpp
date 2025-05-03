#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cout << "Enter the total number of elements => ";
    cin >> n;

    vector<int> arr(n);

    cout << "Enter " << n << " numbers:- \n";
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    for(int i = 0; i < n - 1; i++) {
        int minVal = arr[i];
        int minPos = i;
        for(int j = i + 1; j < n; j++) {
            if(arr[j] < minVal) {
                minVal = arr[j];
                minPos = j;
            }
        }

        int temp = arr[i];
        arr[i] = arr[minPos];
        arr[minPos] = temp;
    }

    cout << "------ Sorted Array is ------ \n";
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
