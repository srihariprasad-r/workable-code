"""
Find length of longest substring with k distinct characters
"""

def longestSubstringUniqueChar(s, m):
  unique_dict = {}
  n = len(s)
  start = 0
  #end = 0
  maxLen = 0
  distinct_cnt = 0

  for i in range(0, n):
    if s[i] not in unique_dict.keys():
      unique_dict[s[i]] = 1
      distinct_cnt += 1
    else: 
      unique_dict[s[i]] += 1

    while(distinct_cnt > m):
      unique_dict[s[start]] -= 1
      if (unique_dict[s[start]] == 0):
        distinct_cnt -= 1
      start += 1 
    #end += 1
    maxLen = max(maxLen, i-start+1)
  return maxLen

s = "eceba"
print(longestSubstringUniqueChar(s, 2))