def find_lcm(first_number, second_number):
    i = 2
    lcm = 1
    while True:
        if first_number % i == 0 and second_number % i == 0:
            lcm *= i

            first_number //= i
            second_number //= i

        elif first_number % i == 0 and second_number % i != 0:
            lcm *= i

            first_number //= i

        elif first_number % i != 0 and second_number % i == 0:
            lcm *= i

            second_number //= i
        else:
            i += 1
        if first_number == 1 and second_number == 1:
            break
    return lcm


first_number = int(input("Number-1:"))
second_number = int(input("Number-2:"))

print("LCM:", find_lcm(first_number, second_number))
