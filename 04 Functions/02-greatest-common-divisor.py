def find_gcd(first_number, second_number):
    i = 1
    gcd = 1
    while i <= first_number and i <= second_number:
        if not (first_number % i) and not (second_number % i):
            gcd = i
        i += 1
    return gcd


first_number = int(input("Number-1:"))
second_number = int(input("Number-2:"))

print("GCD:", find_gcd(first_number, second_number))
