import csv
import re

# correct answers
correct_1_case_marks = '3'
correct_1_punctuation_marks = '2'
correct_1_number_marks = '3'
correct_1_word_count_marks = '17'
correct_1_correct_word_marks = '16'
correct_1_incorrect_word_marks = '1'

correct_2_case_marks = '3'
correct_2_punctuation_marks = '3'
correct_2_number_marks = '0'
correct_2_word_count_marks = '17'
correct_2_correct_word_marks = '17'
correct_2_incorrect_word_marks = '0'

correct_3_case_marks = '3'
correct_3_punctuation_marks = '10'
correct_3_number_marks = '0'
correct_3_word_count_marks = '27'
correct_3_correct_word_marks = '27'
correct_3_incorrect_word_marks = '0'

# Current student marks
file_1_mark = 0
file_2_mark = 0
file_3_mark = 0


# Reset globals
def reset_globals():
    global file_1_mark
    global file_2_mark
    global file_3_mark

    file_1_mark = 0
    file_2_mark = 0
    file_3_mark = 0


# Mark student file by file and produce feedback based on mark brackets
def mark_student(student):
    global file_1_mark
    global file_2_mark
    global file_3_mark

    student_feedback = []
    student = student.rstrip()

    try:
        formatted_file_1 = []

        file_1 = (open(f'./CW_spell/spellcheck_{student}/results_spell/test_file1_{student}.txt', 'r')).readlines()
        for line in file_1:
            formatted_line = re.sub("[^0-9]", "", line)
            print(formatted_line)
            formatted_file_1.append(formatted_line)
    except FileNotFoundError:
        formatted_file_1 = None

    try:
        formatted_file_2 = []

        file_2 = (open(f'./CW_spell/spellcheck_{student}/results_spell/test_file2_{student}.txt', 'r')).readlines()
        for line in file_2:
            formatted_line = re.sub("[^0-9]", "", line)
            formatted_file_2.append(formatted_line)
    except FileNotFoundError:
        formatted_file_2 = None

    try:
        formatted_file_3 = []

        file_3 = (open(f'./CW_spell/spellcheck_{student}/results_spell/test_file3_{student}.txt', 'r')).readlines()

        for line in file_3:
            formatted_line = re.sub("[^0-9]", "", line)
            formatted_file_3.append(formatted_line)
    except FileNotFoundError:
        formatted_file_3 = None


    if formatted_file_1 != None:
        if formatted_file_1[2] == correct_1_case_marks and formatted_file_1[3] == correct_1_punctuation_marks and formatted_file_1[4] == correct_1_number_marks and formatted_file_1[6] == correct_1_word_count_marks and formatted_file_1[7] == correct_1_correct_word_marks and formatted_file_1[8] == correct_1_incorrect_word_marks:
            file_1_mark = 1
            student_feedback.append("Correct checking for file 1\n")
        else:
            student_feedback.append("Incorrect checking for file 1\n")
    else:
        student_feedback.append("No file output or incorrect output format for test file 1\n")

    if formatted_file_2 != None:
        if formatted_file_2[2] == correct_2_case_marks and formatted_file_2[3] == correct_2_punctuation_marks and formatted_file_2[4] == correct_2_number_marks and formatted_file_2[6] == correct_2_word_count_marks and formatted_file_2[7] == correct_2_correct_word_marks and formatted_file_2[8] == correct_2_incorrect_word_marks:
            file_2_mark = 1
            student_feedback.append("Correct checking for file 2\n")
        else:
            student_feedback.append("Incorrect checking for file 2\n")
    else:
        student_feedback.append("No file output or incorrect output format for test file 2\n")

    if formatted_file_3 != None:
        if formatted_file_3[2] == correct_3_case_marks and formatted_file_3[3] == correct_3_punctuation_marks and formatted_file_3[4] == correct_3_number_marks and formatted_file_3[6] == correct_3_word_count_marks and formatted_file_3[7] == correct_3_correct_word_marks and formatted_file_3[8] == correct_3_incorrect_word_marks:
            file_3_mark = 1
            student_feedback.append("Correct checking for file 3\n")
        else:
            student_feedback.append("Incorrect checking for file 3\n")
    else:
        student_feedback.append("No file output or incorrect output format for test file 3\n")



    return student_feedback




# write results to csv output
def write_result(feedback, student):
    f = open('./spell_marks.csv', 'a')
    writer = csv.writer(f)

    results = [student, file_1_mark, file_2_mark, file_3_mark, ''.join(feedback)]

    writer.writerow(results)


if __name__ == '__main__':
    # open/create output file
    with open(
            f"./list_of_students.txt", "r", encoding="utf-8"
    ) as temp_file:
        list_of_students = temp_file.readlines()  # not readlines() because it would include \n

    header = ['Student_number', 'file_1_mark', 'file_2_mark', 'file_3_mark', 'Feedback']
    f = open('./spell_marks.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()

    # Mark students
    for student in list_of_students:
        reset_globals()
        feedback = mark_student(student)
        write_result(feedback, student)
