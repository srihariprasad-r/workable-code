def subseq_lesser_sum(arr, k):
  
  n = len(arr)
  ret = []
  tmp = []

  for i in range(n):
    sum = arr[i]   
    tmp = [arr[i]]
    if arr[i] < k:
      ret.append([arr[i]])
    for j in range(i+1, n):      
        sum  += arr[j] 
        if sum < k:
          tmp.extend([arr[j]])
        else:
          sum -= arr[j]
          continue
    if len(tmp) > 1 : ret.append(tmp)
  return len(ret)



arr = [2, 3, 7, 1, 4, 5]
k = 10
print(subseq_lesser_sum(arr, k))