def is_it_even(number):
    if number % 2 == 0:
        return number
    else:
        raise ValueError


list = [34, 2, 1, 3, 33, 100, 61, 1800]

for i in list:
    try:
        print(is_it_even(i))
    except ValueError:
        pass
