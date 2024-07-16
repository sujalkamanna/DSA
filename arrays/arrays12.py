# reversing array

import array as arr

arr1 = arr.array("i", [1, 2, 3, 4, 5])


def reverse(array):
    array.reverse()
    print(array)


reverse(arr1)

# using


def rev():
    return arr1[::-1]


print(rev())

A = [1, 2, 3, 4, 5, 6]
print(A)


def reverse1(start, end, array):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start = start + 1
        end = end - 1
        print(A)


reverse1(0, 5, arr)
