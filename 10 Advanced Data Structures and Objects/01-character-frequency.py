sentence = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frequency = dict()

for character in sentence:
    if (character in frequency):
        frequency[character] += 1
    else:
        frequency[character] = 1
for i, j in frequency.items():

    print(i, ":", j)
