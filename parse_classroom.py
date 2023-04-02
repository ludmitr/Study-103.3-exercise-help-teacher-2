SIMPLE_CLASSROOM_PATH = "classroom_simple.txt"
COMPLEX_CLASSROOM_PATH = "classroom_complex.txt"


def main():
    student_name_input = input("Enter student name: ")

    # students_list = parse_simple_classroom(SIMPLE_CLASSROOM_PATH)
    students_list = parse_complex_classroom(COMPLEX_CLASSROOM_PATH)
    print(students_list)
    average_grades = student_avg(students_list, student_name_input)

    if average_grades:
        print(f"the average grades of {student_name_input}, {average_grades}")
    else:
        print("Sorry, this user does not exist")


def parse_complex_classroom(file_path):
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
    del students_list[0]  # deleting first element empty string

    # adding student info as dictionary to a students: list
    students = []
    for student_info in students_list:
        student_info = student_info.strip().split("\n")
        name, country = student_info[0], student_info[1]
        grades = [int(grade) for grade in student_info[2:]]

        student_dict = {
            "name": name,
            "country": country,
            "grades": grades
        }
        students.append(student_dict)

    return students


def student_avg(students_list: list, student_name: str):
    """
     Return the average (float) of grades of the student. In case
    student_name doesn't exist in student_list, return None.
    """

    # iterating student_list to find student with name student_name
    # if found -> return average of its student grades
    for student in students_list:
        if student["name"] == student_name:
            grades = student["grades"]
            return round(sum(grades) / len(grades), 1)

    return None  # case where no student["name"] == student_name


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
