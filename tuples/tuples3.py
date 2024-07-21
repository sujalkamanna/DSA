# searching in tuple

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9,)

print(1 in tup)
if 1 in tup:
    print(1)


# linear search
def linear(tup, element):
    for i in range(len(tup)):
        if tup[i] == element:
            return i
    return -1


print(linear(tup, 5))
