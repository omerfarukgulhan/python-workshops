first_exam = int(input("First exam:"))
second_exam = int(input("Second exam:"))
final = int(input("Final:"))


grades_avarage = first_exam * 3 / 10 + second_exam * 3 / 10 + final * 4 / 10

if grades_avarage >= 90:
    print("AA")
elif grades_avarage >= 85:
    print("BA")
elif grades_avarage >= 80:
    print("BB")
elif grades_avarage >= 75:
    print("CB")
elif grades_avarage >= 70:
    print("CC")
elif grades_avarage >= 65:
    print("DC")
elif grades_avarage >= 60:
    print("DD")
elif grades_avarage >= 55:
    print("FD")
else:
    print("FF")
