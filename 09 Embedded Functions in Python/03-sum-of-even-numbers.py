from functools import reduce
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_filter = list(filter(lambda x: x % 2 == 0, numbers_list))

print(reduce(lambda x, y: x + y, sum_filter))
