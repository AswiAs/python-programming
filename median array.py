int main() 
{ 
    int a[] = { 1, 3, 4, 2, 7, 5, 8, 6 }; 
    int n = sizeof(a)/sizeof(a[0]); 
    cout << "Mean = " << findMean(a, n) << endl;  
    cout << "Median = " << findMedian(a, n) << endl;  
    return 0; 
} 
