# finding element in array 

def finf(arr, key):
    for i in range(len(arr1)):
        if arr[i] == key:
            return i
    return -1

arr1 = [12, 34, 10, 6, 40]
n = len(arr1)
key = 34


index = finf(arr1 ,key)
if index != -1:
    print("Element found at position: " + str(index + 1))  # +1 for 1-based index
else:
    print("Element not found")