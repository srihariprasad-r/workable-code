def minelement(A):
    low = 0
    high = len(A) - 1
    N = len(A) 

    while low <= high:
        mid = low + (high-low)//2

        if A[low] <= A[high]:
            return low

        next = (mid+1) % N  # to base it to 0- N
        prev = (mid-1+ N) % N # to avoid negative
        if A[mid] <= A[prev] and A[mid] <= A[next]:
            return mid

        if A[mid] <= A[high]:
            high = mid - 1
        elif A[mid] >= A[low]:
            low = mid  + 1

    return -1 

        
A = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
print(minelement(A))