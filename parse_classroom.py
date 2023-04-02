def main():
    print(parse_simple_classroom("classroom_simple.txt"))


def parse_simple_classroom(file_path):
    # getting all data in one string
    with open(file_path, "r") as file:
        data = file.read()

    # splitting the info so each element in list will represent student information
    students_list = data.split("###")
    del students_list[0]  # first element empty string

    # parse student info from student_list and adding it as dictionary to list variable: students
    students = []
    for student_info in students_list:
        name, country, grade_1, grade_2, grade_3 = student_info.strip().split("\n")
        student_dict = {
                        "name": name,
                        "country": country,
                        "grades": [int(grade_1), int(grade_2), int(grade_3)]
                        }
        students.append(student_dict)

    return students


if __name__ == '__main__':
    main()