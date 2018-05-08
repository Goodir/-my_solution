"""
Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K,
returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8].

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
"""


def solution(A, K):
    a = A[:]
    k = 0
    if A == []:
        return A
    while K > k:
        s = 0
        while True:
            i = s + 1
            if i == len(A):
                a[0] = A[-1]
                break
            a[i] = A[s]
            s += 1
        k += 1
        A = a[:]
    return a
