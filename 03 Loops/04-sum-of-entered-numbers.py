sum = 0
print("Program will calculate sum of the numbers you entered until you type 'q'.")
while True:
    number = input("Number: ")

    if number == "q":
        break
    number = int(number)

    sum += number

print("Sum: ", sum)
