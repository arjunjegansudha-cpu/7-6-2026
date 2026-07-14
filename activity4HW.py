tuple1 = (4, 3, 2, 2, -1, 18)
tuple2 = (2, 4, 8, 8, 3, 2, 9)

result = tuple(a * b for a, b in zip(tuple1, tuple2))

print("Multiplied Tuple:", result)
