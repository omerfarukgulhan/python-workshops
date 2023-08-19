number = int(input("Number: "))

i = 1
sum = 0
while i < number:
    if number % i == 0:
        sum += i
    i += 1

if sum == number:
    print(number, " is perfect number.")
else:
    print(number, " is not a perfect number.")
