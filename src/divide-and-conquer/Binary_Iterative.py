'''
Created on 7 Jan 2020

@author: cybercoolsam
'''

import math
from array import array
def binarySearch(arrToSearch,low,high,keyToSearch):
    while low <=high:
        mid=math.floor(low+(high-low)/2)
        
        if arrToSearch[mid]==keyToSearch:
            return mid
        elif arrToSearch[mid]<keyToSearch:
            low=mid+1
        else:
            high=mid-1
            
    return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")