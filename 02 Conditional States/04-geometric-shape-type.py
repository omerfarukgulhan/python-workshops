shape_type = int(input("How many corners does the shape have?"))

if shape_type == 4:
    print("Please enter the edges in order.")
    first_edge = int(input("Edge-1:"))
    second_edge = int(input("Edge-2:"))
    third_edge = int(input("Edge-3:"))
    fourth_edge = int(input("Edge-4:"))

    if (
        first_edge == second_edge
        and first_edge == third_edge
        and first_edge == fourth_edge
    ):
        print("Square")
    elif first_edge == third_edge and second_edge == fourth_edge:
        print("Rectangle")
    else:
        print("Scalene")

elif shape_type == 3:
    first_edge = int(input("Edge-1:"))
    second_edge = int(input("Edge-2:"))
    third_edge = int(input("Edge-3:"))
    if (
        abs(first_edge + second_edge) > third_edge
        and abs(first_edge + third_edge) > second_edge
        and abs(second_edge + third_edge) > first_edge
    ):
        if first_edge == second_edge and first_edge == third_edge:
            print("Equilateral Triangle...")
        elif (
            (first_edge == second_edge and first_edge != third_edge)
            or (first_edge == third_edge and first_edge != second_edge)
            or (second_edge == third_edge and second_edge != first_edge)
        ):
            print("Isosceles Triangle....")
        else:
            print("A scalene triangle...")
    else:
        print("Doesn't specify a triangle...")

else:
    print("Invalid form...")
