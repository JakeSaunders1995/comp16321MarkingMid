import csv
import os

if __name__ == '__main__':
    top_path = os.getcwd()

    #Create marks file
    header = ['Student_number', 'file_1_mark', 'file_2_mark', 'file_3_mark',
              'Feedback']

    f = open('./rugby_marks.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()

    list_of_students = []
    with open('list_of_students.txt', 'r') as f:
        for line in f:
            list_of_students.append(line.rstrip())

    for student in list_of_students:
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

        os.chdir(f'./CW_rugby/rugby_{student}')
        exist_feed = open(f'./fback.txt', 'r')
        existing_feedback =exist_feed.readlines()


        #if no submission set marks to zero
        if not "No submission was found under the prog1_rugby tag for the rugby task\n" in existing_feedback:

            #Find if any files were create
            files_created = os.listdir(f'./results_rugby')
            if len(files_created) == 0:
               no_created_files = True
            else:
                #check their names

                #File 1

                try:

                    file_1 = (
                        open(f'./results_rugby/test_file1_{student}.txt', 'r')).readline()
                    if file_1 == "0:13":
                        file_1_mark = 1
                    else:
                        incorrect_score_1 = True
                except FileNotFoundError:
                    try:
                        file_1 = (
                            open(f'./results_rugby/test_file1_{student}','r')).readline()
                        if file_1 == "0:13":
                            file_1_mark = 1
                        else:
                            incorrect_score_1 = True
                    except FileNotFoundError:
                        file_1 = None
                        incorrect_name_1 = True

                # File 2
                try:
                    file_2 = (
                        open(f'./results_rugby/test_file2_{student}.txt', 'r')).readline()
                    if file_2 == "15:12":
                        file_2_mark = 1
                    else:
                        incorrect_score_2 = True
                except FileNotFoundError:
                    try:
                        file_2 = (
                            open(f'./results_rugby/test_file2_{student}', 'r')).readline()
                        if file_2 == "15:12":
                            file_2_mark = 1
                        else:
                            incorrect_score_2 = True
                    except FileNotFoundError:
                        file_2 = None
                        incorrect_name_2 = True

                # File 3
                try:
                    file_3 = (
                        open(f'./results_rugby/test_file3_{student}.txt', 'r')).readline()
                    if file_3 == "5:17":
                        file_3_mark = 1
                    else:
                        incorrect_score_3 = True
                except FileNotFoundError:
                    try:
                        file_3 = (
                            open(f'./results_rugby/test_file3_{student}', 'r')).readline()
                        if file_3 == "5:17":
                            file_3_mark = 1
                        else:
                            incorrect_score_3 = True
                    except FileNotFoundError:
                        file_3 = None
                        incorrect_name_3 = True

        #### OUTPUT FEEDBACK
            with open(f'./fback.txt', 'a') as f:
                if no_created_files == True:
                    f.write(
                        "No files were created within the results folder. (This does not mean files were not created elsewhere)\n")

                if incorrect_score_1 == True:

                    f.write("Score output for test_file 1 was incorrect\n")

                if incorrect_name_1 ==True:
                    f.write("Output files were found however no output file was found for test_file 1 with the correct name format\n")

                if incorrect_score_2 == True:
                    f.write("Score output for test_file 2 was incorrect\n")

                if incorrect_name_2 == True:
                    f.write(
                        "Output files were found however no output file was found for test_file 2 with the correct name format\n")

                if incorrect_score_3 == True:
                    f.write("Score output for test_file 3 was incorrect\n")

                if incorrect_name_3 == True:
                    f.write(
                        "Output files were found however no output file was found for test_file 3 with the correct name format\n")




                    f.close()

            #output to csv

            new_feed = open(f'./fback.txt', 'r')
            new_feedback = new_feed.readlines()
            os.chdir(top_path)
            f = open('./rugby_marks.csv', 'a')
            writer = csv.writer(f)
            print(new_feedback)
            print("***")
            results = [student, file_1_mark, file_2_mark, file_3_mark, " ".join(new_feedback)]

            writer.writerow(results)

            f.close()



        else:
            os.chdir(top_path)
            #Output to csv
            f = open('./rugby_marks.csv', 'a')
            writer = csv.writer(f)

            results = [student, file_1_mark, file_2_mark, file_3_mark, " ".join(existing_feedback)]

            writer.writerow(results)

            f.close()

        os.chdir(top_path)


