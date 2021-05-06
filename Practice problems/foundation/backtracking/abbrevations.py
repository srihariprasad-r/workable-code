def subseq(p, cnt=0, ans = '', pos=0):
    if pos == len(p):
        if cnt == 0:
            print(ans)
        else:
            print(ans + str(cnt))
        return
    
    if cnt > 0:
        subseq(p, 0, ans + str(cnt) + p[pos], pos+1)
    else:
        subseq(p, cnt, ans + p[pos], pos+1)
    subseq(p, cnt + 1, ans, pos+1)


p = 'pep'
subseq(p)