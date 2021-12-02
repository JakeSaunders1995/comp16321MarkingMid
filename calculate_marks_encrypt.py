import csv

correct_hex = "a broken clock is right twice a day"
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

    try:
        file_1 = (open(f'./CW_encrypt/decrypt_{student}/results_encrypt/test_file1_{student}.txt', 'r')).readline()
    except FileNotFoundError:
        file_3 = None

    try:
        file_2 = (open(f'./CW_encrypt/decrypt_{student}/results_encrypt/test_file2_{student}.txt', 'r')).readline()
    except FileNotFoundError:
        file_3 = None

    try:
        file_3 = (open(f'./CW_encrypt/decrypt_{student}/results_encrypt/test_file3_{student}.txt', 'r')).readline()
    except FileNotFoundError:
        file_3 = None

    if file_1 != None:
        if file_1 == correct_hex:
            file_1_mark = 1
            student_feedback.append("Correct hex decryption for file 1\n")
        else:
            student_feedback.append("Incorrect hex decryption for file 1\n")
    else:
        student_feedback.append("No file output or incorrect output format for hex file\n")

    if file_2 != None:
        if file_2 == correct_caesar:
            file_2_mark = 1
            student_feedback.append("Correct caesar decryption for file 2\n")
        else:
            student_feedback.append("Incorrect caesar decryption for file 2\n")
    else:
        student_feedback.append("No file output or incorrect output format for caesar file\n")

    if file_3 != None:
        if file_3 == correct_morse:
            file_3_mark = 1
            student_feedback.append("Correct morse decryption for file 3\n")
        else:
            student_feedback.append("Incorrect morse decryption for file 3\n")
    else:
        student_feedback.append("No file output or incorrect output format for morse file\n")

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