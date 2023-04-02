def main():
    students_list = parse_simple_classroom("classroom_simple.txt")

    average_grades = student_avg(students_list, "Griffin")
    print(average_grades)


def student_avg(students_list: list, student_name: str):
    """
     Return the average (float) of grades of the student. In case
    student_name doesn’t exist in student_list, return None.
    """

    grades = None
    for student in students_list:
        if student["name"] == student_name:
            grades = student["grades"]
            break

    return round(sum(grades) / len(grades), 1)


def parse_simple_classroom(file_path):
    """ Parse classroom file that is given in `file_path` parameter.
     Returns a list of dictionaries describing the students in the classroom,
     each student is described with the dictionary: {
       'name': ...,
       'country': ...,
       'grades': [...]
     }"""
    # getting all data in one string
    with open(file_path, mode="r") as file:
        data = file.read()

    # split data so each element in list will represent student information
    students_list = data.split("###")
    del students_list[0]  # first element empty string

    # adding student info as dictionary to a students: list
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
