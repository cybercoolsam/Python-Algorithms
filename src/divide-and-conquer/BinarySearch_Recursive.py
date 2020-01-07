'''
Created on 7 Jan 2020

@author: cybercoolsam
'''

import math

def binarySearch(arrToSearch,low,high,keyToSearch):
    if(high<low):
        return -1
    else:
        mid= math.floor(low+(high-low)/2)
        if arrToSearch[mid]==keyToSearch:
            return mid
        elif arrToSearch[mid] < keyToSearch:
            return binarySearch(arrToSearch, mid+1,high, keyToSearch) 
        else:
            return binarySearch(arrToSearch, low,mid-1, keyToSearch) 


#test
arrToSearch = [ 2, 3, 4, 10, 40 ] 
key = 40
  
# Function call 
result = binarySearch(arrToSearch, 0, len(arrToSearch)-1, key) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")