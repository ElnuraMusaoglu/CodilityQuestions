'''

An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].

'''

def solution(A):
    L = len(A)
    T = int((L + 1)*(L + 2) / 2)
    total = 0

    for i in range(L):
        total += A[i]

    return T - total

print(solution([2,3,1,5]))
print(solution([1, 3]))
