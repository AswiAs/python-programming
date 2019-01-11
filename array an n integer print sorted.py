int main() 
{ 
    int arr[] = {1, 1, 2, 4, 4, 5, 5, 6, 6}; 
    int len = sizeof(arr)/sizeof(arr[0]); 
    search(arr, 0, len-1); 
    return 0; 
} 
