#include <bits/stdc++.h> 
using namespace std; 

int maxDifference(int n, vector<int> a) 
{ 
	 
	int max = a[1] - a[0];
	max = max<0 ? -1 : max;
	
	
	int min = a[0]; 
	for(int i = 1; i < n; i++) 
	{	 
	if (a[i] - min > max)							 
		max = a[i] - min; 
		
	if (a[i] < min) 
		min = a[i];					 
	} 
	
	return max; 
} 

/* Driver program to test above function */
int main() 
{ 
int arr[] = {10,8,7,6,5}; 
int n = sizeof(arr) / sizeof(arr[0]); 
vector<int> vec;
for(int i = 0; i<n; ++i)
	vec.push_back(arr[i]);

cout << "Maximum difference is " << maxDifference(n,vec); 

return 0; 
} 
