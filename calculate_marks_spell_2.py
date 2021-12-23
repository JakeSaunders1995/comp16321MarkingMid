import csv
import os
import re

if __name__ == '__main__':
    top_path = os.getcwd()

    #Create marks file
    header = ['Student_number', 'file_1_mark', 'file_2_mark', 'file_3_mark',
              'Feedback']

    f = open('./spell_marks.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()

    list_of_students = []
    with open('list_of_students.txt', 'r') as f:
        for line in f:
            list_of_students.append(line.rstrip())

    for student in list_of_students:
        print(student)
        file_1_mark = 0
        file_2_mark = 0
        file_3_mark = 0
        existing_feedback = []
        no_created_files = False
        incorrect_name_1 = False
        incorrect_score_1 = False
        incorrect_name_2 = False
        incorrect_score_2 = False
        incorrect_name_3 = False
        incorrect_score_3 = False

        incorrect_case_1 = False
        incorrect_punctuation_1 = False
        incorrect_number_1 = False
        incorrect_wc_1 = False
        incorrect_correct_1 = False
        incorrect_incorrect_1 = False

        incorrect_case_2 = False
        incorrect_punctuation_2 = False
        incorrect_number_2 = False
        incorrect_wc_2 = False
        incorrect_correct_2 = False
        incorrect_incorrect_2 = False

        incorrect_case_3 = False
        incorrect_punctuation_3 = False
        incorrect_number_3 = False
        incorrect_wc_3 = False
        incorrect_correct_3 = False
        incorrect_incorrect_3 = False

        os.chdir(f'./CW_spell/spellcheck_{student}')
        exist_feed = open(f'./fback.txt', 'r')
        existing_feedback =exist_feed.readlines()


        #if no submission set marks to zero
        if not "No submission was found under the prog3_spellchecker tag for the spellchecker task\n" in existing_feedback:

            #Find if any files were create
            files_created = os.listdir(f'./results_spell')
            if len(files_created) == 0:
               no_created_files = True
            else:
                #check their names

                #File 1
                formatted_file_1 = []
                try:

                    file_1 = (
                        open(f'./results_spell/test_file1_{student}.txt', 'r')).readlines()

                    for line in file_1:
                        formatted_line = re.sub("[^0-9]", "", line)
                        formatted_file_1.append(formatted_line)
                    print(formatted_file_1[2])
                    if not formatted_file_1[2] == '3':
                        incorrect_case_1 = True

                    if not formatted_file_1[3] == '2':
                        incorrect_punctuation_1 = True

                    if not formatted_file_1[4] == '3':
                        incorrect_number_1 = True

                    if not formatted_file_1[6] == '17':
                        incorrect_wc_1 = True

                    if not formatted_file_1[7] == '16':
                        incorrect_correct_1 = True

                    if not formatted_file_1[8] == '1':
                        incorrect_incorrect_1 = True



                    if incorrect_case_1 == False and incorrect_punctuation_1 == False and incorrect_number_1 == False and incorrect_wc_1 == False and incorrect_correct_1 == False and incorrect_incorrect_1 == False:
                        file_1_mark = 1
                    else:
                        incorrect_score_1 = True
                except (FileNotFoundError, IndexError):
                    try:
                        file_1 = (
                            open(f'./results_spell/test_file1_{student}','r')).readlines()
                        for line in file_1:
                            formatted_line = re.sub("[^0-9]", "", line)
                            formatted_file_1.append(formatted_line)

                        if not formatted_file_1[2] == '3':
                            incorrect_case_1 = True

                        if not formatted_file_1[3] == '2':
                            incorrect_punctuation_1 = True

                        if not formatted_file_1[4] == '3':
                            incorrect_number_1 = True

                        if not formatted_file_1[6] == '17':
                            incorrect_wc_1 = True

                        if not formatted_file_1[7] == '16':
                            incorrect_correct_1 = True

                        if not formatted_file_1[8] == '1':
                            incorrect_incorrect_1 = True

                        if incorrect_case_1 == False and incorrect_punctuation_1 == False and incorrect_number_1 == False and incorrect_wc_1 == False and incorrect_correct_1 == False and incorrect_incorrect_1 == False:
                            file_1_mark = 1
                        else:
                            incorrect_score_1 = True
                    except FileNotFoundError:
                        file_1 = None
                        incorrect_name_1 = True

                    except IndexError:
                        file_1 = None
                        incorrect_score_1 = True

                formatted_file_2 = []
                # File 2
                try:
                    file_2 = (
                        open(f'./results_spell/test_file2_{student}.txt', 'r')).readlines()
                    for line in file_2:
                        formatted_line = re.sub("[^0-9]", "", line)
                        formatted_file_2.append(formatted_line)

                    if not formatted_file_2[2] == '3':
                        incorrect_case_2 = True

                    if not formatted_file_2[3] == '3':
                        incorrect_punctuation_2 = True

                    if not formatted_file_2[4] == '0':
                        incorrect_number_2 = True

                    if not formatted_file_2[6] == '17':
                        incorrect_wc_2 = True

                    if not formatted_file_2[7] == '17':
                        incorrect_correct_2 = True

                    if not formatted_file_2[8] == '0':
                        incorrect_incorrect_2 = True

                    if incorrect_case_2 == False and incorrect_punctuation_2 == False and incorrect_number_2 == False and incorrect_wc_2 == False and incorrect_correct_2 == False and incorrect_incorrect_2 == False:
                        file_2_mark = 1
                    else:
                        incorrect_score_2 = True
                except (FileNotFoundError, IndexError):
                    try:
                        file_2 = (
                            open(f'./results_spell/test_file2_{student}', 'r')).readlines()
                        for line in file_2:
                            formatted_line = re.sub("[^0-9]", "", line)
                            formatted_file_2.append(formatted_line)

                        if not formatted_file_2[2] == '3':
                            incorrect_case_2 = True

                        if not formatted_file_2[3] == '3':
                            incorrect_punctuation_2 = True

                        if not formatted_file_2[4] == '0':
                            incorrect_number_2 = True

                        if not formatted_file_2[6] == '17':
                            incorrect_wc_2 = True

                        if not formatted_file_2[7] == '17':
                            incorrect_correct_2 = True

                        if not formatted_file_2[8] == '0':
                            incorrect_incorrect_2 = True

                        if incorrect_case_2 == False and incorrect_punctuation_2 == False and incorrect_number_2 == False and incorrect_wc_2 == False and incorrect_correct_2 == False and incorrect_incorrect_2 == False:
                            file_2_mark = 1
                        else:
                            incorrect_score_2 = True
                    except FileNotFoundError:
                        file_2 = None
                        incorrect_name_2 = True

                    except IndexError:
                        file_2 = None
                        incorrect_score_2 = True

                formatted_file_3 = []
                # File 3
                try:
                    file_3 = (
                        open(f'./results_spell/test_file3_{student}.txt', 'r')).readlines()
                    for line in file_3:
                        formatted_line = re.sub("[^0-9]", "", line)
                        formatted_file_3.append(formatted_line)

                    if not formatted_file_3[2] == '3':
                        incorrect_case_3 = True

                    if not formatted_file_3[3] == '10':
                        incorrect_punctuation_2 = True

                    if not formatted_file_3[4] == '0':
                        incorrect_number_3 = True

                    if not formatted_file_3[6] == '27':
                        incorrect_wc_3 = True

                    if not formatted_file_3[7] == '27':
                        incorrect_correct_3 = True

                    if not formatted_file_3[8] == '0':
                        incorrect_incorrect_3 = True

                    if incorrect_case_3 == False and incorrect_punctuation_3 == False and incorrect_number_3 == False and incorrect_wc_3 == False and incorrect_correct_3 == False and incorrect_incorrect_3 == False:
                        file_3_mark = 1
                    else:
                        incorrect_score_3 = True
                except (FileNotFoundError, IndexError):
                    try:
                        file_3 = (
                            open(f'./results_spell/test_file3_{student}', 'r')).readlines()
                        for line in file_3:
                            formatted_line = re.sub("[^0-9]", "", line)
                            formatted_file_3.append(formatted_line)

                        if not formatted_file_3[2] == '3':
                            incorrect_case_3 = True

                        if not formatted_file_3[3] == '10':
                            incorrect_punctuation_2 = True

                        if not formatted_file_3[4] == '0':
                            incorrect_number_3 = True

                        if not formatted_file_3[6] == '27':
                            incorrect_wc_3 = True

                        if not formatted_file_3[7] == '27':
                            incorrect_correct_3 = True

                        if not formatted_file_3[8] == '0':
                            incorrect_incorrect_3 = True

                        if incorrect_case_3 == False and incorrect_punctuation_3 == False and incorrect_number_3 == False and incorrect_wc_3 == False and incorrect_correct_3 == False and incorrect_incorrect_3 == False:
                            file_3_mark = 1
                        else:
                            incorrect_score_3 = True
                    except FileNotFoundError:
                        file_3 = None
                        incorrect_name_3 = True

                    except IndexError:
                        file_3 = None
                        incorrect_score_3 = True

        #### OUTPUT FEEDBACK
            with open(f'./fback.txt', 'a') as f:
                if no_created_files == True:
                    f.write(
                        "No files were created within the results folder. (This does not mean files were not created elsewhere)\n")

                if incorrect_score_1 == True:

                    f.write("Output for test_file 1 was incorrect\n")

                if incorrect_name_1 ==True:
                    f.write("Output files were found however no output file was found for test_file 1 with the correct name format\n")


                if incorrect_case_1 == True:
                    f.write("Case count was incorrect for test_file1\n")

                if incorrect_punctuation_1 == True:
                    f.write("Punctuation count was incorrect for test_file1\n")

                if incorrect_number_1 == True:
                    f.write("Number count was incorrect for test_file1\n")

                if incorrect_wc_1 == True:
                    f.write("Word count was incorrect for test_file1\n")

                if incorrect_correct_1 == True:
                    f.write("Correct word count was incorrect for test_file1\n")

                if incorrect_incorrect_1 == True:
                    f.write("Incorrect word count was incorrect for test_file1\n")

                if incorrect_score_2 == True:
                    f.write("Output for test_file 2 was incorrect\n")

                if incorrect_name_2 == True:
                    f.write(
                        "Output files were found however no output file was found for test_file 2 with the correct name format\n")

                if incorrect_case_2 == True:
                    f.write("Case count was incorrect for test_file2\n")

                if incorrect_punctuation_2 == True:
                    f.write("Punctuation count was incorrect for test_file2\n")

                if incorrect_number_2 == True:
                    f.write("Number count was incorrect for test_file2\n")

                if incorrect_wc_2 == True:
                    f.write("Word count was incorrect for test_file2\n")

                if incorrect_correct_2 == True:
                    f.write("Correct word count was incorrect for test_file2\n")

                if incorrect_incorrect_2 == True:
                    f.write("Incorrect word count was incorrect for test_file2\n")

                if incorrect_score_3 == True:
                    f.write("Output for test_file 3 was incorrect\n")

                if incorrect_name_3 == True:
                    f.write(
                        "Output files were found however no output file was found for test_file 3 with the correct name format\n")

                if incorrect_case_3 == True:
                    f.write("Case count was incorrect for test_file3\n")

                if incorrect_punctuation_3 == True:
                    f.write("Punctuation count was incorrect for test_file3\n")

                if incorrect_number_3 == True:
                    f.write("Number count was incorrect for test_file3\n")

                if incorrect_wc_3 == True:
                    f.write("Word count was incorrect for test_file3\n")

                if incorrect_correct_3 == True:
                    f.write("Correct word count was incorrect for test_file3\n")

                if incorrect_incorrect_3 == True:
                    f.write("Incorrect word count was incorrect for test_file3\n")

                    f.close()

            #output to csv

            new_feed = open(f'./fback.txt', 'r')
            new_feedback = new_feed.readlines()
            os.chdir(top_path)
            f = open('./spell_marks.csv', 'a')
            writer = csv.writer(f)

            results = [student, file_1_mark, file_2_mark, file_3_mark, " ".join(new_feedback)]

            writer.writerow(results)

            f.close()



        else:
            os.chdir(top_path)
            #Output to csv
            f = open('./spell_marks.csv', 'a')
            writer = csv.writer(f)

            results = [student, file_1_mark, file_2_mark, file_3_mark, " ".join(existing_feedback)]

            writer.writerow(results)

            f.close()

        os.chdir(top_path)


