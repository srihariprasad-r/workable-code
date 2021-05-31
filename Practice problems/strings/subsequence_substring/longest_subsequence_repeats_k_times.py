def longestsubseqrepeatsktimes(s1, k):
    i = j = 0
    freq_dct = {}

    for c in s1:
        if c not in freq_dct:
            freq_dct[c] = 1
        else:
            freq_dct[c] += 1

    for c in s1:
        if freq_dct[c] >= k:
            print(c, end="")
    print("\n")



s = 'geeksforgeeks'
print(longestsubseqrepeatsktimes(s, 2))