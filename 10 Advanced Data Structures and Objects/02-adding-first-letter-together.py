first_letters = ""

with open("poem.txt", "r", encoding="utf-8") as file:
    for line in file:
        first_letters += line[0]
print(first_letters)
