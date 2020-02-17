"""Input:

{3,4,-1,3,1,3,1,-1,-2,-2}

subarray with 0 sum are: 
{3,4,-7}
{4,-7,3}
{-7,3,1,3}
{3,1,-4}
{3,1,3,1,-4,-2,-2}
{3,4,-7,3,1,3,1,-4,-2,-2}
"""

def zero_sum_subarray(array):
    prevlist = [0]
    occurance = {}
    for i in array:
        prevlist.append(prevlist[-1]+i)

    for j in prevlist:
        if j in occurance:
            occurance[j] += 1
        else:
            occurance[j] = 1

    return sum((v*(v-1))//2 for v in occurance.values())


array =  [3,4,-7,3,1,3,1,-1,-2,-2]
output = zero_sum_subarray(array)
print(output)