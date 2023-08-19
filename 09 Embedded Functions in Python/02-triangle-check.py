def is_it_triangle(array):

    if (abs(array[0]+array[1]) > array[2] and abs(array[0]+array[2]) > array[1] and abs(array[1]+array[2]) > array[0]):
        return True
    else:
        return False


triangle_list = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]

print(list(filter(is_it_triangle, triangle_list)))
