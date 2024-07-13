array = [1, 2, 3, 4, 5]

print("constant time complexity")
print(array[0])


print("\nlinear time complexity")
for elements in array:
    print(elements)

print("\nlogarithmetic time complexity")
for index in range(0, len(array), 3):
    print(array[index])


print("\nquadratic time complexity")
for x in array:
    for y in array:
        print(x, y)

print("\exponential time complexity")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(5))

print("\nadd vs multiply")


array_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array_b = [11, 12, 13, 14, 15, 16, 17, 18, 19]

for a in array_a:
    print(a)

for b in array_b:
    print(b)

for a in array_a:
    for b in array_b:
        print(a, b)

sample_array = [86, 6, 321, 78, 54, 897, 333333, 4, 54, 12]


def find_biggest_no(sample_array):
    biggest_no = sample_array[0]
    for index in range(1, len(sample_array)):
        if sample_array[index] > biggest_no:
            biggest_no = sample_array[index]
    print(biggest_no)


find_biggest_no(sample_array)


def biggest_no(sample_array2):
    print(max(sample_array2))


sample_array2 = [86, 6, 321, 78, 54, 897, 333333, 4, 54, 12]

biggest_no(sample_array2)
