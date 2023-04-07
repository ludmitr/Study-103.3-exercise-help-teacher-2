import statistics
SIMPLE_CLASSROOM_PATH = "classroom_simple.txt"
COMPLEX_CLASSROOM_PATH = "classroom_complex.txt"


def main():
    """
    parsing on COMPLEX_CLASSROOM_PATH
    """
    # getting students dictionary out of COMPLEX_CLASSROOM_PATH and printing statistics
    students = parse_complex_classroom(COMPLEX_CLASSROOM_PATH)
    print(calculate_statistics_of_classroom(students))

    # getting name from user, printing he's average grade and all info we have on him
    student_name_input = input("Enter student name: ")
    average_grades = student_avg(students, student_name_input)
    if average_grades:
        print(f"the average grades of {student_name_input}, {average_grades}")
        print(students[student_name_input])
    else:
        print("Sorry, this user does not exist")


def calculate_statistics_of_classroom(students: dict):
    """
    Calculate statistics of classroom - total average grade, median grade,
    and sorted students by its average grade.
    returns:  string with all statistics
    """
    # putting all grades together
    all_grades = []
    for student_info in students.values():
        all_grades.extend(student_info["grades"])

    total_average_grade = calculate_average_of_grades(all_grades)
    median_grade = calculate_median_grade(all_grades)
    sorted_student_list = sort_student_by_average_grade(students)

    # creating text with statics of classroom
    text_to_print = (
        "Total average of grades: {}\n"
        "Median grade: {}\n"
        "Student by average grade, from highest to lowest:"
    ).format(total_average_grade, median_grade)
    for student in sorted_student_list:
        text_to_print += f"\nname: {student['name']}, average grade: {student['av_grade']}"

    return text_to_print


def sort_student_by_average_grade(students: dict):
    """
    Calculate the average grade for each student and return the result as a list of dictionaries.

    Each dictionary in the returned list has the following format:
    {
        "name": "student_name",
        "av_grade": average_grade: float
    }
    """
    # creating list of dictionaries with student info
    student_list = []
    for student_name, info in students.items():
        student = {
                   "name": student_name,
                   "av_grade": calculate_average_of_grades(info["grades"])
                  }
        student_list.append(student)

    # sorting list by its average grades from high to low
    sorted_student_list = sorted(
                        student_list,
                        key=lambda student_info: student_info["av_grade"],
                        reverse=True)

    return sorted_student_list


def calculate_median_grade(grades: list):
    """
    Calculate median grade and returns it
    """
    sorted_grades = sorted(grades)
    return statistics.median(sorted_grades)


def calculate_average_of_grades(grades: list):
    """
    returns an average grade(float) of grades
    """
    return round(sum(grades) / len(grades), 1)


def parse_complex_classroom(file_path):
    """ Parse classroom file that is given in `file_path` parameter.
     Returns a dictionary of dictionaries describing the students in the classroom,
     where keys are name of student and value is dict of info of that student
     each student is described with the dictionary: {
        'country': ...,
        'grades': [...] list of int
        'notes': [...,...]
        'additional attributes': ...
    }"""
    # getting all data in one string
    with open(file_path, mode="r") as file:
        data = file.read()

    # split data so each element in list will represent student information
    students_list = data.split("###")
    del students_list[0]  # deleting first element empty string

    # adding student info as dictionary to a students dictionary
    students = {}
    for student_info in students_list:
        student_dict = {}
        student_info = student_info.strip().split("\n")
        name, student_dict["country"] = student_info[0], student_info[1]
        grades = []
        notes = []
        for index in range(2, len(student_info)):
            if student_info[index].isnumeric():  # case where rest info is grades:
                grades = [int(grades) for grades in student_info[index:]]
                break
            # adding arbitrary attributes, creating notes
            key, value = student_info[index].split("=")
            if key == "note":
                notes.append(value)
            else:
                student_dict[key] = value

        if notes:
            student_dict["notes"] = notes
        student_dict["grades"] = grades
        students[name] = student_dict

    return students


def student_avg(students_dict: dict, student_name: str):
    """
     Return the average (float) of grades of the student. In case
    student_name doesn't exist in student_list, return None.
    """

    # iterating student_list to find student with name student_name
    # if found -> return average of its student grades
    if student_name in students_dict:
        grades = students_dict[student_name]["grades"]
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
