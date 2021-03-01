"""
let arr: [1, 2, 3, 4]

k = -1 => [2, 3, 4, 1]
k = 0 => [1, 2, 3, 4]
k = 1 => [4, 1, 2, 3]
k = 2 => [3, 4, 1, 2]
k = 3 => [2, 3, 4, 1]
k = 4 => [1, 2, 3, 4]
k = 5 => [4, 1, 2, 3]

so, k = 4 and k = 0 are the same, which means k = k % len(arr)

if, we have k < 0, k = k + len(arr) , refer k = -1 and k = 3

use this formular, and split the array into 2 parts

P1 = 0 to len(arr) - k -1
P2 = len(arr) - k to len(arr) -1 

first reverse P2 and then rever P1, finally do total reverse of entire array to get array rotation
"""

def rotatearray(arr, k):
    def reverse(arr, l, r):
        while l < r:
            tmp = arr[l]
            arr[l] = arr[r]
            arr[r] = tmp
            l += 1
            r -= 1
        # return arr
        
    k = k % len(arr)
    if k < 0:
        k = k + len(arr)
    
    reverse(arr, 0, len(arr)-k-1)
    reverse(arr, len(arr)-k, len(arr)-1)
    reverse(arr, 0, len(arr)-1)
    
    return arr

arr = [1, 2, 3, 4, 5]
k = 2
print(rotatearray(arr, k))