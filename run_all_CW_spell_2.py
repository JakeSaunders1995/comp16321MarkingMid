import os
import subprocess
from fnmatch import fnmatch

if __name__ == '__main__':

    top_path  = os.getcwd()



    default_path = os.getcwd()
    #format the files into folders and add test files and reuslt folder

    list_of_students = []
    with open('list_of_students.txt', 'r') as f:
        for line in f:
            list_of_students.append(line.rstrip())





    # Make file structure
    for student in list_of_students:
        if not os.path.exists(f'./CW_spell/spellcheck_{student}'):
            os.mkdir(f'./CW_spell/spellcheck_{student}')

            #Make tesfiles folder
            make_input = ['mkdir', f'./CW_spell/spellcheck_{student}/test_files_spell', ]
            subprocess.call(make_input)
            #Make results folder

            #copy test files into test files folder
            copy_input = ['cp', '-r', f'./test_files_spell', f'./CW_spell/spellcheck_{student}', ]
            subprocess.call(copy_input)
            #Create feedback file


        if not os.path.exists(f'./CW_spell/spellcheck_{student}/EnglishWords.txt'):
            cpew= ['cp', f'./EnglishWords.txt', f'./CW_spell/spellcheck_{student}', ]
            subprocess.call(cpew)

        #Delete and remake results files
        if os.path.exists(f'./CW_spell/spellcheck_{student}/results_spell'):
            df = ['rm', '-r', f'./CW_spell/spellcheck_{student}/results_spell', ]
            subprocess.call(df)
        make_input2 = ['mkdir', f'./CW_spell/spellcheck_{student}/results_spell', ]
        subprocess.call(make_input2)

        #Delete and remake feedback files on new run

        if os.path.exists(f'./CW_spell/spellcheck_{student}/fback.txt'):
            feedbacks = ['rm', f'./CW_spell/spellcheck_{student}/fback.txt', ]
            subprocess.call(feedbacks)
            feedback = ['touch', f'./CW_spell/spellcheck_{student}/fback.txt', ]
            subprocess.call(feedback)
        else:
            feedback = ['touch', f'./CW_spell/spellcheck_{student}/fback.txt', ]
            subprocess.call(feedback)

        # search all direcotry and subdirectorys to find py files in the unpackked repo
        print(student)
        for path, subdirs, files in os.walk(f'./unpacked_repos/{student}_prog3_spellchecker'):
            for name in files:
                if fnmatch(name, "*.py"):
                    move_input = ['cp', f'{path}/{name}', f'./CW_spell/spellcheck_{student}']
                    subprocess.call(move_input)


    count = 0
    #run the courseworks
    for student in list_of_students:

        file_exists = False
        correct_program_name = False
        time_out = False
        errors = ""

        count+=1


        print(f'Running {student}')

        #Check python file exists
        os.chdir(f'./CW_spell/spellcheck_{student}')
        py_files = os.listdir(f'./')
        for file in py_files:
            if file.endswith('.py'):
                file_exists = True

                if file == (f'spellcheck_{student}.py'):
                    correct_program_name = True




                    inputs = ['python3', f'./spellcheck_{student}.py', './EnglishWords.txt', './test_files_spell', './results_spell']
                    ###subprocess.call(inputs)
                    res = subprocess.Popen(inputs, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        output, error = res.communicate(timeout=60)
                        errors = error.decode("utf-8")
                        errors = errors.replace("/home/jake/Desktop/repos/Marking/CW_spell", "***Removed due to privacy***")
                        print(errors)
                    except subprocess.TimeoutExpired:
                        time_out = True

                    #fix error messages

        #Write feedback
        print(os.getcwd())
        with open(f'./fback.txt', 'a') as f:
            if file_exists == False:
                f.write("No submission was found under the prog3_spellchecker tag for the spellchecking task\n")
            else:
                if correct_program_name == False:
                    f.write("Submission was found under the prog3_spellchecker tag for the spellchecking  task but the file is named incorrectly\n")

            if time_out == True:
                f.write("Submission ran indefinitely and did not finish its execution. \nThis does not mean the program did not execute it may or may not have produced some files or none\n")


            if not errors == "":
                f.write(f'Submission ran but did not finish its execution due to the errors below. \nThis does not mean the program did not execute however, it may or may not have produced some files or none: \n\n {errors}\n')

            f.close()

        os.chdir(top_path )

    print(count)