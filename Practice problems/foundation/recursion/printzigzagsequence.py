"""
Pre sequence is peformed while going up recursive stack
In sequence is performed between left and right call
Post sequence is performed while coming down recursive stack
"""
def printzigzagsequence(n):
    if n == 0:
        return
    print("pre sequence:", n)        # pre-sequence
    printzigzagsequence(n-1)  # left call
    print("in sequence:", n)            # in sequence
    printzigzagsequence(n-1)  # right call
    print("post sequence:", n)            # post sequence

n = 3
printzigzagsequence(n)