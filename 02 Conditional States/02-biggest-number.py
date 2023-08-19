first_number = int(input("first number:"))

second_number = int(input("second number:"))

third_number = int(input("first number:"))

if first_number >= second_number and first_number >= third_number:
    print("Biggest number:", first_number)
elif second_number >= first_number and second_number >= third_number:
    print("Biggest number:", second_number)
elif third_number >= first_number and third_number >= second_number:
    print("Biggest number:", third_number)
