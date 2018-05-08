"""
Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example,
given N = 1041 the function should return 5,
because N has binary representation 10000010001
and so its longest binary gap is of length 5.

Assume that:

N is an integer within the range [1..2,147,483,647].
"""


def solution(N):
    N = bin(N)[2:]
    res = []
    i = 0
    for a in N:
        if a == '0':
            i += 1
        elif (a == '1' and i != 0) or res == []:
            res.append(i)
            i = 0
    res.sort()
    return res[-1]
