import csv
import re

# correct answers
correct_1_case_marks = '4'
correct_1_punctuation_marks = '5'
correct_1_number_marks = '0'
correct_1_word_count_marks = '54'
correct_1_correct_word_marks = '54'
correct_1_incorrect_word_marks = '0'

correct_2_case_marks = '5'
correct_2_punctuation_marks = '9'
correct_2_number_marks = '4'
correct_2_word_count_marks = '30'
correct_2_correct_word_marks = '28'
correct_2_incorrect_word_marks = '2'

correct_3_case_marks = '4'
correct_3_punctuation_marks = '10'
correct_3_number_marks = '3'
correct_3_word_count_marks = '65'
correct_3_correct_word_marks = '62'
correct_3_incorrect_word_marks = '3'

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

    studnet_feedback = []

    # mark file 1
    formatted_file_1 = []
    try:
        student = student.rstrip()

        file_1 = (open(f'results_spell/test_file1_{student}', 'r')).readlines()
    except FileNotFoundError:
        file_1 = None


        
        for line in file_1:
            formatted_line = re.sub("[^0-9]", "", line)
            formatted_file_1.append(formatted_line)

        if formatted_file_1[2] == correct_1_case_marks:
            case_marks = case_marks + 1

        if formatted_file_1[3] == correct_1_punctuation_marks:
            punctuation_marks = punctuation_marks + 1

        if formatted_file_1[4] == correct_1_number_marks:
            number_marks = number_marks + 1

        if formatted_file_1[6] == correct_1_word_count_marks:
            word_count_marks = word_count_marks + 1

        if formatted_file_1[7] == correct_1_correct_word_marks:
            correct_word_marks = correct_word_marks + 1

        if formatted_file_1[8] == correct_1_incorrect_word_marks:
            incorrect_word_marks = incorrect_word_marks + 1



        # mark file 2
        formatted_file_2 = []

        file_2 = (open(f'results_spell/test_file2_{student}', 'r')).readlines()

        for line in file_2:
            formatted_line = re.sub("[^0-9]", "", line)
            formatted_file_2.append(formatted_line)

        if formatted_file_2[2] == correct_2_case_marks:
            case_marks = case_marks + 1

        if formatted_file_2[3] == correct_2_punctuation_marks:
            punctuation_marks = punctuation_marks + 1

        if formatted_file_2[4] == correct_2_number_marks:
            number_marks = number_marks + 1

        if formatted_file_2[6] == correct_2_word_count_marks:
            word_count_marks = word_count_marks + 1

        if formatted_file_2[7] == correct_2_correct_word_marks:
            correct_word_marks = correct_word_marks + 1

        if formatted_file_2[8] == correct_2_incorrect_word_marks:
            incorrect_word_marks = incorrect_word_marks + 1

        # mark file 3
        formatted_file_3 = []

        file_3 = (open(f'results_spell/test_file3_{student}', 'r')).readlines()

        for line in file_3:
            formatted_line = re.sub("[^0-9]", "", line)
            formatted_file_3.append(formatted_line)

        if formatted_file_3[2] == correct_3_case_marks:
            case_marks = case_marks + 1

        if formatted_file_3[3] == correct_3_punctuation_marks:
            punctuation_marks = punctuation_marks + 1

        if formatted_file_3[4] == correct_3_number_marks:
            number_marks = number_marks + 1

        if formatted_file_3[6] == correct_3_word_count_marks:
            word_count_marks = word_count_marks + 1

        if formatted_file_3[7] == correct_3_correct_word_marks:
            correct_word_marks = correct_word_marks + 1

        if formatted_file_3[8] == correct_3_incorrect_word_marks:
            incorrect_word_marks = incorrect_word_marks + 1




        return studnet_feedback




# write results to csv output
def write_result(feedback, student):
    f = open('./spell_marks.csv', 'a')
    writer = csv.writer(f)

    results = [student, word_count_marks, correct_word_marks, incorrect_word_marks
        , case_marks, punctuation_marks, number_marks, ''.join(feedback)]

    writer.writerow(results)


if __name__ == '__main__':
    # open/create output file
    with open(
            f"./list_of_students.txt", "r", encoding="utf-8"
    ) as temp_file:
        list_of_students = temp_file.readlines()  # not readlines() because it would include \n

    header = ['Student_number', 'word_count_marks', 'Correct_word_marks', 'incorrect_word_marks'
        , 'case_marks', 'punctuation_marks', 'Number_marks', 'Feedback']
    f = open('./spell_marks.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()

    # Mark students
    for student in list_of_students:
        reset_globals()
        feedback = mark_student(student)
        write_result(feedback, student)
