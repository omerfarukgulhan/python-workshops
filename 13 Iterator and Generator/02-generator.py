def is_it_prime(number):
    i = 2

    while i < number:
        if (number % i == 0):
            return False
        i += 1
    return True


def prime_generator():
    i = 2
    while True:
        if (is_it_prime(i)):
            yield i
        i += 1


for number in prime_generator():
    if (number > 1000):
        break
    print(number)
