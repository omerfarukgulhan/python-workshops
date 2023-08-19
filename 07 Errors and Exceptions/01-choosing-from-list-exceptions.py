list = ["345", "book", "324a", "14", "kemal"]

for element in list:
    try:
        element = int(element)
        print(element)
    except:
        pass
