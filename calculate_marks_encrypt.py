import csv

correct_hex = "solving hex is very easy in python"
correct_caesar = "but caesar is a little more difficult"
correct_morse = "however solving morse code may be the most difficult"

#Globals
hex_mark = 0
caesar_mark = 0
morse_mark = 0

#Reset globals
def reset_globals():
    global hex_mark
    global caesar_mark
    global morse_mark

    hex_mark = 0
    caesar_mark = 0
    morse_mark = 0

def mark_student(student):
    global hex_mark
    global caesar_mark
    global morse_mark

    student_feedback = []

    file_1 = (open(f'results_encrypt/test_file1_{student}', 'r')).readline()
    file_2 = (open(f'results_encrypt/test_file2_{student}', 'r')).readline()
    file_3 = (open(f'results_encrypt/test_file3_{student}', 'r')).readline()

    if file_1 == correct_hex:
        hex_mark = 5
        student_feedback.append("Correct hex decrypt")
    else:
        student_feedback.append("Incorrect hex decrypt")

    if file_2 == correct_caesar:
        caesar_mark = 5
        student_feedback.append("Correct caesar decrypt")
    else:
        student_feedback.append("Incorrect caesar decrypt")

    if file_3 == correct_morse:
        morse_mark = 5
        student_feedback.append("Correct morse decrypt")
    else:
        student_feedback.append("Incorrect morse decrypt")

    return student_feedback

def write_result(feedback, student):
    f = open('./encrypt_marks.csv', 'a')
    writer = csv.writer(f)

    results = [student, hex_mark,caesar_mark,morse_mark, ''.join(feedback)]

    writer.writerow(results)

if __name__ == '__main__':
    # Open/create marks file
    with open(
            f"./list_of_students.txt", "r", encoding="utf-8"
    ) as temp_file:
        list_of_students = temp_file.readlines()  # not readlines() because it would include \n

    header = ['Student_number', 'hex_mark', 'caesar_mark', 'Morse_mark',
              'Feedback']
    f = open('./encrypt_marks.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()

    # Mark students
    for student in list_of_students:
        student = student.strip()
        reset_globals()
        feedback = mark_student(student)
        write_result(feedback, student)