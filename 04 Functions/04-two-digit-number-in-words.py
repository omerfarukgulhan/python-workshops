ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
tens = [
    "",
    "Ten",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
]


def read(number):
    first = number % 10
    second = number // 10
    return tens[second] + " " + ones[first]


number = int(input("Number(two digit):"))

print(read(number))
