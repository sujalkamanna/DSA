#array left rotation

arr = [1,2,3,4,5,6,7,8,9]
def left_rotate(arr ,d):
    n = len(arr)
    d = d%n
    rotated_array = arr[d:] + arr[:d]
    return rotated_array


rotated_array = left_rotate(arr,2)
print(rotated_array)