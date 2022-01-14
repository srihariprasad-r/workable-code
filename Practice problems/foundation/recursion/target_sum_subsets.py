def recursion(idx, arr, tgt, ans=0, lst=[], res = []):
    if idx == len(arr):
        if ans == tgt:
            if lst in res:
                return

            res.append(lst)
        return res
    
    for i in range(idx, len(arr)):
        recursion(i + 1, arr, tgt, ans +  arr[i], lst+[i] , res)
        recursion(i + 1, arr, tgt, ans, lst)

    return res
    
arr = [15, 10, 20, 30, 5 , 25, 15]
print(recursion(0, arr, 30))