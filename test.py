array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = [2, 5, 7, 9, 4, 2, 5, 5, 6, 9]

print(list(filter(lambda x: True if x % 2 == 0 else False, array)))
print(list(map(lambda x: x**2 if x % 2 == 0 else x, array)))

array3 = [(1, 4), (3, 2), (5, 2), (0, 6)]
print(list(map(lambda x: (x[1], x[0]), array3)))
print(sorted(array3, key=lambda x: (x[1], -x[0])))
print(max(array3, key=lambda x: x[1]))
