import heapq

def kmaximumsumsubarray(arr, k):
    cursum = 0
    res = []
    
    for i in range(len(arr)):
        j = i + 1
        cursum = arr[i]
        res.append(cursum)
        while j < len(arr):
            cursum += arr[j]
            res.append(cursum)
            j += 1
        
    heaplst = [-x for x in res]
    heapq.heapify(heaplst)
    
    for i in range(k):
        res = -heapq.heappop(heaplst)
        print(res)
            

arr = [4, -8, 9, -4, 1, -8, -1, 6]
print(kmaximumsumsubarray(arr, 4))