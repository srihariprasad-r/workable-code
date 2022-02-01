def combinations(idx, list1, list2, list3, visited, ans=[], res=[]):
    if idx > len(list1) - 1:
        res.append(' '.join(ans))
        return

    if visited[idx]:
        combinations(idx+1, list1, list2, list3)
    else:
        visited[idx] = True
        for j in range(len(list2)):
            ans.append(list1[idx] + ' ' + list2[j] + ' ' + list3[j])
            combinations(idx + 1, list1, list2, list3, visited, ans, res)
            ans.pop()
        visited[idx] = False

    return res


list1 = ['John', 'Emma']
list2 = ['Plays', 'Hates', 'Watches']
list3 = ['Cricket', 'Soccer', 'Chess']
visited = [False for _ in range(len(list1))]
print(combinations(0, list1, list2, list3, visited))
"""
['John Plays Cricket 
Emma Plays Cricket', 
'John Plays Cricket
Emma Hates Soccer', 
'John Plays Cricket 
Emma Watches Chess', 
'John Hates Soccer 
Emma Plays Cricket', 
'John Hates Soccer
Emma Hates Soccer', 
'John Hates Soccer 
Emma Watches Chess', 
'John Watches Chess 
Emma Plays Cricket', 
'John Watches Chess
Emma Hates Soccer', 
'John Watches Chess
Emma Watches Chess']
"""
