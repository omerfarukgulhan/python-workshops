def extra(func):

    def extra_feature():
        print("Perfect numbers...")
        for number in range(1, 1001):
            sum = 0
            i = 1
            while (i < number):
                if (number % i == 0):
                    sum += i
                i += 1
            if (sum == number):
                print(number)
        func()

    return extra_feature


@extra
def prime_numbers():
    print("Prime numbers...")
    for number in range(2, 1001):
        i = 2
        temp = 0
        while (i < number):
            if (number % i == 0):
                temp += 1
            i += 1
        if (temp == 0):
            print(number)


prime_numbers()
