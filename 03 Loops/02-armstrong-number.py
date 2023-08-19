number = input("Number: ")
number_digits = len(str(number))
number = int(number)
digit = 0
sum = 0
temp = number

while temp > 0:
    digit = temp % 10

    sum += digit**number_digits

    temp //= 10

if sum == number:
    print(number, " is armstrong number.")
else:
    print(number, " is not a armstrong number.")
