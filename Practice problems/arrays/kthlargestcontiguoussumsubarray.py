import heapq

def kthlargestcontiguoussum(arr, k):
    suffixsum = []
    
    for i in range(len(arr)):
        j = i + 1
        suffixsum.append(arr[i])
        while j < len(arr):
            suffixsum.append(suffixsum[-1]  + arr[j])
            j += 1
            
    heaplst = [-x for x in suffixsum]
    heapq.heapify(heaplst)
    
    for i in range(k):
        res = -heapq.heappop(heaplst)
        
    return res


arr = [20, -5, -1]
print(kthlargestcontiguoussum(arr, 3))