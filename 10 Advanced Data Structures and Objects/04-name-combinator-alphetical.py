name = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]

surname = ["Yılmaz", "Öztürk", "Dağdeviren",
           "Atatürk", "Dikmen", "Kaya", "Polat"]

combined_list = list(zip(name, surname))

combined_list.sort()

for i, j in combined_list:
    print(i, j)
