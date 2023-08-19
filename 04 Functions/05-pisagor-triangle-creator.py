def find_pisagor():
    pisagor_list = list()
    for i in range(1, 101):
        for j in range(1, 101):
            hypotenuse = (i**2 + j**2) ** 0.5

            if hypotenuse == int(hypotenuse):
                pisagor_list.append((i, j, int(hypotenuse)))

    return pisagor_list


for i in find_pisagor():
    print(i)
