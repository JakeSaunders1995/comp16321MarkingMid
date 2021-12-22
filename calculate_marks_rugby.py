import csv

# Correct marks for marking students
correct_1 = "0:13"
correct_2 = "15:12"
correct_3 = "5:17"

# Current student marks
file_1_mark = 0
file_2_mark = 0
file_3_mark = 0



# Reset student marks after finishing each student
def reset_globals():
    global file_1_mark
    global file_2_mark
    global file_3_mark


    file_1_mark = 0
    file_2_mark = 0
    file_3_mark = 0

# Mark the student via reading their file and comparing with correct marks
def mark_student(student):
    global file_1_mark
    global file_2_mark
    global file_3_mark

    student_feedback = []


    student = student.rstrip()
    print(student)
    #Checking that the files exist and if so reads them
    try:
        file_1 = (open(f'./CW_rugby/rugby_{student}/results_rugby/test_file1_{student}.txt', 'r')).readline()
    except FileNotFoundError:
        file_1 = None

    try:
        file_2 = (open(f'./CW_rugby/rugby_{student}/results_rugby/test_file2_{student}.txt', 'r')).readline()
    except FileNotFoundError:
        file_2 = None

    try:
        file_3 = (open(f'./CW_rugby/rugby_{student}/results_rugby/test_file3_{student}.txt', 'r')).readline()
    except FileNotFoundError:
        file_3 = None

    if file_1 != None:
        if file_1 == correct_1:
            file_1_mark = 1
            student_feedback.append("Correct score for file 1\n")
        else:
            student_feedback.append("Incorrect score for file 1\n")
    else:
        student_feedback.append("No file output or incorrect output format for test file 1\n")

    if file_2 != None:
        if file_2 == correct_2:
            file_2_mark = 1
            student_feedback.append("Correct score for file 2\n")
        else:
            student_feedback.append("Incorrect score for file 2\n")
    else:
        student_feedback.append("No file output or incorrect output format for test file 2\n")

    if file_3 != None:
        if file_3 == correct_3:
            file_3_mark = 1
            student_feedback.append("Correct score for file 3\n")
        else:
            student_feedback.append("Incorrect score for file 3\n")
    else:
        student_feedback.append("No file output or incorrect output format for test file 3\n")




    return student_feedback



# Output the marks to CSV per student
def write_result(feedback, student):
    f = open('./rugby_marks.csv', 'a')
    writer = csv.writer(f)

    results = [student, file_1_mark, file_2_mark, file_3_mark, ''.join(feedback)]

    writer.writerow(results)


if __name__ == '__main__':

    # Open/create marks file
    with open(
            f"./list_of_students.txt", "r", encoding="utf-8"
    ) as temp_file:
        list_of_students = temp_file.readlines()  # not readlines() because it would include \n

        header = ['Student_number', 'file_1_mark', 'file_2_mark', 'file_3_mark',
                  'Feedback']

        f = open('./rugby_marks.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(header)
        f.close()

        # Mark students
        for student in list_of_students:
            reset_globals()
            feedback = mark_student(student)
            write_result(feedback, student)
