from collections import deque

q1 = deque()
q2 = deque()
q3 = deque()


def threearraytriplet(arr1, arr2, arr3):
    start2, start3 = 0, 0
    min_diff2 = float('inf')
    min_diff3 = float('inf')
    diff = float('inf')
    for i in range(len(arr1)):
        start2, start3 = 0, 0

        while start2 < len(arr1):
            if abs(arr1[i] - arr2[start2]) < min_diff2:
                min_diff2 = abs(arr1[i] - arr2[start2])
                if len(q2) == 0:
                    q2.append(arr2[start2]) 
                else: 
                    q2.pop() 
                    q2.append(arr2[start2])
            start2 += 1

        while start3 < len(arr1):
            if abs(arr1[i] - arr3[start3]) < min_diff3:
                min_diff3 = abs(arr1[i] - arr3[start3])
                if len(q3) == 0:
                    q3.append(arr3[start3]) 
                else: 
                    q3.pop() 
                    q3.append(arr3[start3])
            start3 += 1

        if abs(min_diff2 + min_diff3) < diff:
            diff = abs(min_diff2 + min_diff3)
            if len(q1) > 0:
                q1.pop()
            q1.append(arr1[i])

    print(q1, q2, q3)
    

arr1 = [15, 12, 18, 9]
arr2 = [10, 17, 13, 8]
arr3 = [14, 16, 11, 5]
threearraytriplet(arr1, arr2, arr3)