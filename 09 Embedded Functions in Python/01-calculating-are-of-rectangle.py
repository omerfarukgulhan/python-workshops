def calculate_area(array):
    return array[0] * array[1]


number_list = [(3, 4), (10, 3), (5, 6), (1, 9)]

print(list(map(calculate_area, number_list)))
