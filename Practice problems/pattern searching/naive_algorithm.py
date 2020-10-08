def naive_algorithm(s, p):
  n = len(s)
  m = len(p)
  for i in range(n-m+1):
    j = 0
    while j < m:
      if s[i+j] != p[j]:        
        break
      j += 1
    if j == m:
      print(i)



text = "abcdabcabcdf"
pattern = "abcdf"
print(naive_algorithm(text, pattern))