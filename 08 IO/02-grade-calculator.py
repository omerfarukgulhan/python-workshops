def calculate_grade(row):


    row = row[:-1]

    list = row.split(",")

    name = list[0]

    grade1 = int(list[1])

    grade2 = int(list[2])

    grade3 = int(list[3])

    final_grade = grade1 * (3/10) + grade2 * (3/10) + grade3 * (4/10)

    if (final_grade >= 90):

        letter_grade = "AA"
    elif (final_grade >= 85):
        letter_grade = "BA"
    elif (final_grade >= 80):
        letter_grade = "BB"
    elif (final_grade >= 75):
        letter_grade = "CB"
    elif (final_grade >= 70):
        letter_grade = "CC"
    elif (final_grade >= 65):
        letter_grade = "DC"
    elif (final_grade >= 60):
        letter_grade = "DD"
    elif (final_grade >= 55):
        letter_grade = "FD"
    else:
        letter_grade = "FF"

    return name + "------------------> " + letter_grade + "\n"







with open("file.txt","r",encoding= "utf-8") as file:

    final_list = []

    for i in file:

        final_list.append(calculate_grade(i))

    with open("grades.txt","w",encoding="utf-8") as grade_file:

        for i in final_list:
            grade_file.write(i)



