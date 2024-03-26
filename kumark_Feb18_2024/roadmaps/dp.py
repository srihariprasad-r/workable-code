# question link: https://docs.google.com/document/d/13ydHMmLXcvIbpvH-rn-9F3Oc4IiekKu8ItLr05HZRJI/edit
# wrong submission
n = 15

y = 100
x = 1 # /7 
z = 50 # /3
b = 100000 # /5

m = n
dp = [0] * 16
dp[1] = y

def min_cost(dp, m):
    n = 2
    while n <= m:

        e1 = 100000001
        e2 = 100000001
        e3 = 100000001
        
        dp[n // 1] += y

        if n % 7 == 0:
            e1 = dp[n//7] + x
            
        if n % 3 == 0:
            e2 = dp[n//3] + z
    
        if n % 5 == 0:
            e3 = dp[n//5] + b

        v = min(dp[n//1], min(e1, min(e2, e3)))

        dp[n] = v
        n += 1

    return dp[m] 
    
print(min_cost(dp, m))

# question link: https://www.desiqna.in/13822/google-dp-interview-question-jan-2023
arr = [5, 4, 2, 6, 12]
# arr = [2, 3, 5, 8, 10]

prefix = [0] * len(arr)
prefix[0] = arr[0]

def odd_sum_count(arr, prefix):
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
        
    # 0 -> 1 -> 2 = prefix[2]
    # 0 -> 2 = prefix[2] - prefix[1] + prefix[0] = prefix[i] - prefix[i-1] + prefix[i-2]
    # 0 -> 1 -> 3 = prefix[3] - prefix[2] + prefix[1] = 17 - 11 + 9 = 15
    
    dp = [0] * len(arr)
    dp[0] = 1 if prefix[0] % 2 else 0
    dp[1] = 1 if prefix[1] % 2 else 0
    
    for i in range(2, len(arr)):
        for j in range(1,3):
            if j == 1: 
                dp[i] += dp[i-1] if prefix[i] % 2 else 0
            else:
                dp[i] += dp[i-2] if (prefix[i] - prefix[i-1] + prefix[i-2]) % 2 else 0
                
    return dp[-1]
    
print(odd_sum_count(arr, prefix))

# question link: https://www.desiqna.in/16115/google-interview-problem-dynamic-programming-cities-october#google_vignette
# A = [23, 4,5 ,101] 
# B = [21,1,10, 100]

A = [25,10,15,10,70] 
B = [5,5,50,5,30]

dp = [0] * len(A)

dp[0] = max(A[0], B[0])

def travel_city(A,B, dp):
    placework = 'A' if A[0] > B[0] else 'B'
    for i in range(1, len(A)):
        if placework == 'A':
            if dp[i-1] + A[i] > dp[i-2] + B[i]:
                dp[i] = A[i] + dp[i-1]
            else:
                dp[i-1] = dp[i-2]
                dp[i] = dp[i-2] + B[i]
                placework = 'B'
        else:
            if dp[i-2] +A[i] > dp[i-1] + B[i]:
                placework = 'A'
                dp[i-1] = dp[i-2]
                dp[i] = dp[i-2] + A[i]
            else:
                dp[i] = B[i] + dp[i-1]
                
    return dp[-1]
                
print(travel_city(A, B, dp))

# question link: https://leetcode.com/discuss/interview-question/4355676/help-needed
A = [
    [1, 2,13, 0],
    [15, 26,7,48],
    [99,86,11,12],
    [92,89,0,99]
]
arr = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

def players(A, arr):
    mx = 0
    
    for i in range(len(A)-1, -1, -1):
        for j in range(len(A)-1, -1, -1):
            up = A[i][j] - A[i-1][j]
            left = A[j][j] - A[i-1][j]
            arr[i][j]= max(up, left)
            mx = max(mx, arr[i][j])
            
    return mx
    
print(players(A, arr))


# question link: https://leetcode.com/problems/palindromic-substrings/
def countSubstrings(s):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    cnt = 0
    l = 1
    for i in range(len(s)):
        dp[i][i] = 1
        cnt += 1
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            cnt += 1
        i += 1
    l = 3
    while l <= len(s):
        i = 0
        while i < len(s) - l + 1:
            j = i + l - 1
            if s[i] == s[j] and dp[i+1][j-1] == 1:
                dp[i][j] =  1
                cnt += 1
            i += 1
        l += 1
    return cnt

# question link: https://www.geeksforgeeks.org/longest-palindromic-substring-using-dynamic-programming/
# s= 'abbabba'
def longestPalindrome(s):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

    ans = 0
    mx = ''
    for i in range(len(s)):
        dp[i][i] = 1
        if ans < 1:
            ans = 1
            mx = s[i]

    l = 1
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            if ans < 2 :
                ans = 2
                mx = s[i:i+ans]
        i += 1

    l = 3
    while l <= len(s):
        i = 0
        while i < len(s) - l + 1:
            j = i + l - 1
            if s[i] == s[j] and dp[i+1][j-1] == 1:
                dp[i][j] = 1
                mx = s[i:i+l]
            i += 1
        l += 1

    return mx

print((longestPalindrome(s)))

# question link: https://leetcode.com/problems/burst-balloons/submissions/904703007/
arr = [3, 1, 5, 8]
mx = float('-inf')
dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]

def burstballons(arr):
    for i in range(len(arr)):
        dp[i][i] = ((arr[i]) * (arr[i-1] if i -1 > -1 else 1) * (arr[i+1] if i + 1 < len(arr) else 1))
        
    l = 2
    while l <= len(arr):
        i = 0
        while i <= len(arr) - l:
            j = i + l - 1
            k = i
            while k <= j:
                s = ((arr[i-1] if i-1>-1 else 1) * (arr[k])* (arr[j+1] if j + 1 < len(arr) else 1))
                s += dp[i][k-1] if k - 1 >= i else 0
                s += dp[k+1][j] if k + 1 <= j else 0
                dp[i][j] = max(dp[i][j], s)
                k += 1
            i += 1
        l += 1
        
    return dp[0][len(arr)-1]
    
print(burstballons(arr))

# question link: https://www.desiqna.in/15592/microsoft-oa-sde-1-dp-freshers-hiring-43-lac-ctc
arr = [1, 9, 8, 9, 5, 1, 2]
dp = [[[0]*3 for _ in range(len(arr))] for _ in range(len(arr))]

s1 = arr[0] + arr[1] # first two elements
s2 = arr[0] + arr[-1] # first and last elements
s3 = arr[-1] + arr[-2] # last two elements

def max_deletes_same_sum(arr, dp):
    for i in range(len(arr)-1):
        s = arr[i] + arr[i+1]
        if  s == s1:
            dp[i][i+1][0] = 1
        elif s == s2:
            dp[i][i+1][1] = 1
        elif s == s3:
            dp[i][i+1][2] = 1
            
    l = 3
    while l <= len(arr):
        i = 0
        while i < len(arr) - l + 1:
            j = i + l - 1
            s = arr[i] + arr[i+1]
            if s == s1:
                dp[i][j][0] = max(dp[i][j][0], 1 + dp[i+2][j][0])
            if s == s2:
                dp[i][j][1] = max(dp[i][j][1], 1 + dp[i+2][j][1])
            if s == s3:
                dp[i][j][2] = max(dp[i][j][2], 1 + dp[i+2][j][2])
            s = arr[i] + arr[j]
            if s == s1:
                dp[i][j][0] = max(dp[i][j][0], 1 + dp[i+1][j-1][0])
            if s == s2:
                dp[i][j][1] = max(dp[i][j][1], 1 + dp[i+1][j-1][1])
            if s == s3:
                dp[i][j][2] = max(dp[i][j][2], 1 + dp[i+1][j-1][2])
            s = arr[j-1] + arr[j]
            if s == s1:
                dp[i][j][0] = max(dp[i][j][0], 1 + dp[i][j-2][0])
            if s == s2:
                dp[i][j][1] = max(dp[i][j][1], 1 + dp[i][j-2][1])
            if s == s3:
                dp[i][j][2] = max(dp[i][j][2], 1 + dp[i][j-2][2])
                
            i += 1
        l += 1
        
    return max(dp[0][len(arr)-1][0], max(dp[0][len(arr)-1][1], dp[0][len(arr)-1][2]))
    
print(max_deletes_same_sum(arr, dp))

# question link: https://leetcode.com/contest/biweekly-contest-108/problems/partition-string-into-minimum-beautiful-substrings/
# wrong submission
def minimumBeautifulSubstrings(s):
    powersOf5 = [format(5**i,'b')  for i in range(15)]
    dp = [0] * len(s)
    dp[0] = 1 if s[0] == '1' else 0
    for i in range(1,len(s)):
        j = i
        t = s[j]
        if s[i] == '0': continue
        v = float('inf')
        while j > -1:
            if str(t) in powersOf5:  
                v = min(v, 1 + dp[j-1])
            j -= 1
            t += s[j]
        dp[i] =  v
    
    return dp[len(s)-1] if dp[len(s)-1] != 0 else -1

s = '111'
print(minimumBeautifulSubstrings(s))