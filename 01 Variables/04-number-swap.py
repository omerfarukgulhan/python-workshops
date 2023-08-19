first_input = input("first number:")
second_input = input("second number:")

print(
    "Numbers before swapping\nfirst number: {} second number: {}\n".format(
        first_input, second_input
    )
)

temp = first_input
first_input = second_input
second_input = temp

print(
    "Numbers after swapping\nfirst number: {} second number: {}\n".format(
        first_input, second_input
    )
)
