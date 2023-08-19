def perfect(number):
    sum = 0

    for i in range(1, number):
        if number % i == 0:
            sum += i

    return sum == number


for i in range(1, 1001):
    if perfect(i):
        print("Perfect number:", i)
