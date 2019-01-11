int main() 
{ 
    int arr[] = { 10, 7, 9, 2, 8, 3, 5, 4, 6, 1 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
  
    
    sortit(arr, n); 
   
    for (int i = 0; i < n; i++)  
        cout << arr[i] << " ";     
} 
